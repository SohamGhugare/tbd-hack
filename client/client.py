import websockets
import asyncio

async def connect():
    async with websockets.connect("ws://localhost:8080/ws") as ws:
        await ws.send("Hello")
        print("Message sent!")

    while True:
        response = await ws.recv()
        print("Received message:", response)

asyncio.get_event_loop().run_until_complete(connect())
