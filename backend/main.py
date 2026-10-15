from fastapi import FastAPI, WebSocket,WebSocketDisconnect
from websocket_manager import ConnectionManager
from auth import verify_token

app = FastAPI()

manager = ConnectionManager()

# @app.websocket("/ws/{user_id}")
# async def websocket_endpoint(user_id:str,websocket:WebSocket):
    
#     await manager.connect(user_id,websocket)
    
#     try:
        
#         while True:
        
#             data = await websocket.receive_json()
            
#             receiver_id = data.get("receiver_id")
#             message = data.get("message")
            
#             await manager.send_private_message(
#                 receiver_id,
#                 {
#                     "sender_id":user_id,
#                     "message":message
                
#                 }
#             )
    
#     except WebSocketDisconnect:
        
#         manager.disconnect(user_id)





@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    
    token = websocket.query_params.get("token")
    
    if not token:
        await websocket.close(code=1008)
        return
    
    user_id = verify_token(token)
    
    if not user_id:
        await websocket.close(code=1008)
        return
    
    await manager.connect(user_id,websocket)
    
    try:
        
        while True:
            
            data = await websocket.receive_json()
            
            receiver_id = data.get("receiver_id")
            message = data.get("message")
            
            await manager.send_private_message(
                receiver_id,
                {
                    "sender_id":user_id,
                    "message": message
                }
                
            )
            
    except WebSocketDisconnect:
        
        manager.disconnect(user_id)
        

# @app.websocket("/ws")
# async def websocket_endpoint(websocket:WebSocket):
    
#     token = websocket.query_params.get("token")
    
#     if not token:
#         await websocket.close(code=1008)
#         return
    
#     user_id = verify_token(token)
    
#     if not user_id:
#         await websocket.close(code=1008)
#         return
    
#     await manager.connect(user_id, websocket)
    
#     try:
        
#         while True:
            
#             data = await websocket.receive_json()
            
#             receiver_id = data.get("receiver_id")
#             message = data.get("message")
            
#             await manager.send_private_message(
#                 receiver_id,
#                 {
#                     "sender_id": user_id,
#                     "message": message
#                 }
#             )
            
#     except WebSocketDisconnect:
#         manager.disconnect(user_id)
        
    