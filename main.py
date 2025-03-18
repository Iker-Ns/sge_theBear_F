from typing import List
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/users/", response_model=List[dict])
async def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result

@app.put("/users/{id}", response_model=dict)
def update_user(id: int, name: str, email: str, db: Session = Depends(get_db)):
    result = user.uptade_user(id, name, email, db)
    return result

@app.delete("/users/{id}", response_model=dict)
def delete_user(id: int, db: Session = Depends(get_db)):
    result = user.delete_user(id, db)
    return result