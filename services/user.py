from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db: Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name:str, email:str, db: Session):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Created user succesfully"}

def uptade_user(id:int, name:str, email:str, db: Session):
    user = db.get(User, id)
    user.name = name
    db.commit()
    db.refresh(user)
    return {"message": "Uptaded user succesfully"}

def delete_user(id:int, db: Session):
    db.delete(User, id)
    db.commit()
    db.refresh(User)
    return {"message": "Deleted user succesfully"}
