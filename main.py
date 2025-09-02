import asyncio
import websockets
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8080))

async def handler(websocket):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"🚀 WebSocket server running at ws://{HOST}:{PORT}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
