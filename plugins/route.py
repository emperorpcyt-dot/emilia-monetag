#(©)Codexbotz
#rymme





from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("CodeXBotz")


@routes.get("/health", allow_head=True)
async def health_handler(request):
    return web.json_response({"status": "ok"})
