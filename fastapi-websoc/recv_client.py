import asyncio
import websockets

async def connect():
    uri = "ws://127.0.0.1:8080/"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = await websocket.recv()
            print(f"<<< {msg}")

if __name__ == "__main__":
    asyncio.run(connect())