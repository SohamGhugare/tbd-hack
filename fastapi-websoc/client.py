import asyncio
import websockets

room_id = input("Enter room code: ")

async def connect(room_id):
    uri = "ws://127.0.0.1:8080/{room_id}/ws"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to room {room_id}")
        while True:
            msg = input(">>> ")

            # Exiting 
            if msg == "exit":
                break

            await websocket.send(msg)

            res = await websocket.recv()
            print(f"<<< {res}")

if __name__ == "__main__":
    asyncio.run(connect())