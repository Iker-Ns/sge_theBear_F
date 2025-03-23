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

def uptade_user(id:int, name:str, db: Session):
    sql_select = select(User).where(User.id == id)
    user_db = db.exec(sql_select).one()

    user_db.name = name
    db.add(user_db)
    db.commit()
    return {"message": "Uptaded user succesfully"}

def delete_user(id:int, db: Session):
    sql_select = select(User).where(User.id == id)
    user_db = db.exec(sql_select).one()

    db.delete(user_db)
    db.commit()
    return {"message": "Deleted user succesfully"}
