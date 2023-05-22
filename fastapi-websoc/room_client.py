import websockets
import asyncio
from managers.room_manager import RoomManager

manager = RoomManager()

async def connect():
    code = int(input("Enter room code: "))
    async with manager.get_connection(code) as websocket:
        print(f"Connected to room {code}")
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