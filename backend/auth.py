# from jose import JWTError,jwt

# SECRET_KEY = "myfather-hero"
# ALGORITHM = "HS256"

# def verify_token(token:str):
    
#     try:
        
#         payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        
#         user_id = payload.get("sub")

#         if user_id is None:
#             return None
        
#         return user_id
    
#     except JWTError:
#         return None

