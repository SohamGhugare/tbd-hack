import json

def get_rooms():
    with open("data/rooms.json", "r") as f:
        return json.load(f)
    
def append_room(room_id):
    data = get_rooms()
    data["rooms"].append(str(room_id))
    with open("data/rooms.json", "w") as f:
        json.dump(data, f)
