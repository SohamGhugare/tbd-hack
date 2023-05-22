from fastapi import WebSocket
from typing import List

class ConnectionManager:
    """
        CONNECTION MANAGER
        Contains all the websocket operations/utility functions for managing multiple concurrent connections.
    """
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    # Accepting a connection
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        
        self.active_connections.append(websocket)

    # Disconnecting from a connection
    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    # Sending a personal message to a websocket connection
    async def send_pm(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    # Sending a message to all connections
    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)