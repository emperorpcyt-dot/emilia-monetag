#(©)Codexbotz
#@iryme





from aiohttp import web
from .route import routes
from .ad_verify import verify_routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    web_app.add_routes(verify_routes)
    return web_app
