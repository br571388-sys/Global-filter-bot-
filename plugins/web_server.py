from aiohttp import web

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.router.add_get("/", health_check)
    return web_app

async def health_check(request):
    return web.Response(text="Bot is alive!")
