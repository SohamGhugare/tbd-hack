from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from manager import ConnectionManager
from datetime import datetime
import json
import uvicorn

app = FastAPI()
manager = ConnectionManager()

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)