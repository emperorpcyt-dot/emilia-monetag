# Ad verification web routes (Telegram Mini App + Monetag rewarded ads)
#
#   GET  /verify              -> the Mini App page (webapp/verify.html)
#   POST /api/verify/start    -> user pressed "watch ad"   (remember time)
#   POST /api/verify/done     -> ad finished               (mark verified + send files)
#
# Every POST carries Telegram's signed initData, so nobody can fake another user.

import os
import time
import hmac
import json
import hashlib
from urllib.parse import parse_qsl

from aiohttp import web

from config import TG_BOT_TOKEN, MONETAG_ZONE, MONETAG_SDK, MONETAG_SDK_URL, MIN_AD_SECONDS, LOGGER
from database.database import clear_ad_started, set_ad_started, get_ad_started, pop_pending
from helper_func import send_files

verify_routes = web.RouteTableDef()

_HTML_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "webapp", "verify.html")


def check_init_data(init_data):
    """Validate Telegram WebApp initData. Returns the user dict, or None if fake/expired."""
    try:
        data = dict(parse_qsl(init_data or "", strict_parsing=True))
    except ValueError:
        return None
    received_hash = data.pop("hash", None)
    if not received_hash:
        return None
    check_string = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
    secret = hmac.new(b"WebAppData", TG_BOT_TOKEN.encode(), hashlib.sha256).digest()
    calc = hmac.new(secret, check_string.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(calc, received_hash):
        return None
    if time.time() - int(data.get("auth_date", 0)) > 3600:
        return None
    try:
        return json.loads(data.get("user", "{}")) or None
    except ValueError:
        return None


@verify_routes.get("/verify")
async def verify_page(request):
    with open(_HTML_PATH, encoding="utf-8") as f:
        html = (f.read()
                .replace("__SDK_URL__", MONETAG_SDK_URL)
                .replace("__ZONE__", MONETAG_ZONE)
                .replace("__SDK__", MONETAG_SDK))
    return web.Response(text=html, content_type="text/html")


@verify_routes.post("/api/verify/start")
async def verify_start(request):
    body = await request.json()
    user = check_init_data(body.get("initData"))
    if not user:
        return web.json_response({"ok": False, "error": "invalid session"}, status=403)
    await set_ad_started(user["id"])
    return web.json_response({"ok": True})


@verify_routes.post("/api/verify/done")
async def verify_done(request):
    body = await request.json()
    user = check_init_data(body.get("initData"))
    if not user:
        return web.json_response({"ok": False, "error": "invalid session"}, status=403)

    user_id = user["id"]
    started = await get_ad_started(user_id)
    if not started or time.time() - started < MIN_AD_SECONDS:
        return web.json_response({"ok": False, "error": "ad not fully watched"}, status=400)

    await clear_ad_started(user_id)          # one ad unlocks one file link
    pending, verify_msg_id = await pop_pending(user_id)
    if not pending:
        return web.json_response({"ok": False, "error": "no file request found, open the file link again"}, status=400)

    client = request.app["bot"]
    # delete the "Watch a short ad..." message now that the ad is done
    if verify_msg_id:
        try:
            await client.delete_messages(user_id, verify_msg_id)
        except Exception:
            pass
    try:
        await client.send_message(user_id, "✅ <b>Vᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟ!</b>")
        await send_files(client, user_id, pending)
    except Exception as e:
        LOGGER(__name__).warning(f"verify_done send failed: {e}")
    return web.json_response({"ok": True})
