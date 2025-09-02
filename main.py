import asyncio
import websockets
import os
from aiohttp import web

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8080))

# --- WebSocket handler ---
async def ws_handler(websocket):
    async for message in websocket:
        await websocket.send(message)  # simple echo, no prints

# --- HTTP handler (for health check) ---
async def http_handler(request):
    return web.Response(text="ok", content_type="text/plain")

async def main():
    # WebSocket server
    await websockets.serve(ws_handler, HOST, PORT)

    # HTTP server for health checks
    app = web.Application()
    app.add_routes([web.get("/", http_handler), web.head("/", http_handler)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, HOST, PORT)
    await site.start()

    await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
