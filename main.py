from fastapi import Depends,FastAPI,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

@app.get("/test/")
async def read(name:str):
    return name