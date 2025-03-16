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