# from fastapi import WebSocket

# class ConnectionManager:
    
#     def __init__(self):
#         self.active_connections = {}
#         self.rooms = {}
        
#     async def connect(self,user_id:str, websocket:WebSocket):
         
#         await websocket.accept()
#         self.active_connections[user_id] = websocket
        
#     def disconnect(self, user_id:str): 
#         if user_id in self.active_connections:
#             del self.active_connections[user_id]
        
#     async def send_message(
#         self,
#         message:str,
#         websocket:WebSocket  
#     ):
#         await websocket.send_text(message)
        
#     async def broadcast(self, data:str):

        
#         for connection in self.active_connections:
#             await connection.send_json(data)


#     async def send_private_message(self, user_id:str, message:dict):
#         websocket = self.active_connections.get(user_id)
        
#         if websocket:
#             await websocket.send_json(message)
            
#     async def join_room(self, room_id:str,user_id:str, websocket:WebSocket):
#         await websocket.accept()
        
#         if room_id not in self.rooms:
#             self.rooms[room_id] = {}
        
#         self.rooms[room_id][user_id] = websocket
        
#     async def broadcast_to_room(self, room_id:str,message:dict):
#         room = self.rooms.get(room_id)
    
#         if not room:
#             return
        
#         for websocket in room.values():
            
#             await websocket.send_json(message)
        
        
from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections = {}
        self.rooms = {}
        
    async def connect(self,user_id:str, websocket:WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        
    def disconnect(self,user_id:str):
        
        if user_id in self.active_connections:
            del self.active_connections[user_id]
            
    async def broadcast(self, data:str):
        for connection in self.active_connections:
            await connection.send_json(data)
            
    async def send_private_message(self, user_id:str, messaage:dict):
        websocket = self.active_connections.get(user_id)
        
        if websocket:
            await websocket.send_json(messaage)
            
    async def join_room(self, room_id:str, user_id:str, websocket:WebSocket):
        await websocket.accept()
        
        if room_id not in self.rooms:
            self.rooms[room_id] = {}
            
        self.rooms[room_id][user_id] = websocket
        
    async def broadcast_to_room(self,room_id:str,message:dict):
        room = self.rooms.get(room_id)
        
        if not room:
            return
        
        for websocket in room.values():
            await websocket.send_json(message)
            
    