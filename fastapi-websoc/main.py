from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from managers.socket_manager import ConnectionManager
from datetime import datetime
import json
import uvicorn
from utility.codegen import generate_room_id
from managers.room_manager import RoomManager

import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

app = FastAPI()
manager = ConnectionManager()
room_manager = RoomManager()

# Adding CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"data": "Hello World"}

@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    now = datetime.now().strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            message = {
                "time": now,
                "message": data
            }
            await manager.broadcast(json.dumps(message))
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        message = {
            "time": now,
            "message":"Offline"
        }
        await manager.broadcast(json.dumps(message))

@app.websocket("/{room_id}/ws")
async def room_endpoint(websocket: WebSocket, room_id: int):
    await manager.connect(websocket)
    now = datetime.now().strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            message = {
                "time": now,
                "message": data,
                "room": room_id
            }
            await manager.broadcast(json.dumps(message))
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        message = {
            "time": now,
            "message":"Offline"
        }
        await manager.broadcast(json.dumps(message))

@app.get("/room/create")
async def create_room():
    room_id = generate_room_id()
    room_manager.add_room(room_id=room_id)
    return {
        "message": "room created",
        "room_id": room_id
    }
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)