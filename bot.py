# fix for current pyrogram 
from pyrogram import utils

def get_peer_type_new(peer_id: int) -> str:
    peer_id_str = str(peer_id)
    if not peer_id_str.startswith("-"):
        return "user"
    elif peer_id_str.startswith("-100"):
        return "channel"
    else:
        return "chat"
utils.get_peer_type = get_peer_type_new#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCESUB_CHANNEL, FORCESUB_CHANNEL2, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        # Start the web server first so Koyeb's health check passes while the bot logs in
        web_app = await web_server()
        web_app["bot"] = self          # lets the ad-verify routes send files
        self.web_runner = web.AppRunner(web_app)
        await self.web_runner.setup()
        await web.TCPSite(self.web_runner, "0.0.0.0", PORT).start()
        self.LOGGER(__name__).info(f"Web server running on port {PORT}")

        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCESUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL)
                    link = (await self.get_chat(FORCESUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCESUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCESUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Hunters_Discussion for support")
                sys.exit()
        if FORCESUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL2)
                    link = (await self.get_chat(FORCESUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCESUB_CHANNEL2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCESUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Hunters_Discussion for support")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/Hunters_Discussion for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Animes_X_Hunters")
        self.LOGGER(__name__).info(f""" \n\n       
░█████╗░███╗░░██╗██╗███╗░░░███╗███████╗██╗░░██╗██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░░██████╗
██╔══██╗████╗░██║██║████╗░████║██╔════╝██║░░██║██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝
███████║██╔██╗██║██║██╔████╔██║█████╗░░███████║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝╚█████╗░
██╔══██║██║╚████║██║██║╚██╔╝██║██╔══╝░░██╔══██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗░╚═══██╗
██║░░██║██║░╚███║██║██║░╚═╝░██║███████╗██║░░██║╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░
                                          """)
        self.username = usr_bot_me.username
        from config import AD_VERIFY, WEBAPP_URL
        if AD_VERIFY:
            self.LOGGER(__name__).info(f"Ad verification ON  ->  {WEBAPP_URL}/verify")
        else:
            self.LOGGER(__name__).info("Ad verification OFF (set MONETAG_ZONE and WEBAPP_URL to enable)")

    async def stop(self, *args):
        await super().stop()
        try:
            await self.web_runner.cleanup()
        except Exception:
            pass
        self.LOGGER(__name__).info("Bot stopped.")
