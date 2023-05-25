from fastapi import WebSocket
from utility import rooms
import websockets

class RoomManager:
    """
        ROOM MANAGER
        This class contains the code for managing all rooms
    """

    def add_room(self, room_id: int):
        rooms.append_room(room_id)

    def get_connection(self, room_id: int):
        if room_id in list(map(int, rooms.get_rooms()["rooms"])):
            return websockets.connect(f"ws://127.0.0.1:8080/{room_id}/ws")
        else:
            print("Room does not exist")
            return
