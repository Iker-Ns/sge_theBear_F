from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()
              
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result


@app.get("/users/")
async def read_user(db: Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/",response_model=dict)
async def create_user(name: str, email: str, db: Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users/",response_model=dict)
async def update_item(id:int, name:str, db: Session = Depends(get_db)):
    result = user.update_user(id, name, db)
    return result

@app.delete("/users/", response_model=dict)
async def delete_item(id:int, db: Session = Depends(get_db)):
    result = user.delete_user(id, db)
    return result 