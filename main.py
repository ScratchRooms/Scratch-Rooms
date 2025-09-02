import os
from aiohttp import web

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8080))

# --- WebSocket handler ---
async def ws_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            await ws.send_str(msg.data)  # echo back
        elif msg.type == web.WSMsgType.BINARY:
            await ws.send_bytes(msg.data)

    return ws

# --- HTTP handler (for health checks) ---
async def http_handler(request):
    return web.Response(text="ok", content_type="text/plain")

app = web.Application()
app.add_routes([
    web.get("/", http_handler),
    web.get("/ws", ws_handler),  # WebSocket endpoint
])

if __name__ == "__main__":
    web.run_app(app, host=HOST, port=PORT)
