from schema.users_sch import users_schema
from sqlmodel import Session, select, update, delete
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users

def add_new_user(name:str,email:str, db:Session):
    db_user = User(name=name,email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Created user succesfully"}

def update_user(id:int,name:str,email:str, db:Session):
    sql_update = select(User).where(User.id == id)
    results = db.exec(sql_update)
    user = results.one()
    user.name = name
    user.email = email
    db.commit()
    db.refresh(user)
    return {"Usuario actualizado con exito"}

def delete_user(id:int, db:Session):
    slq_delete = delete(User).where(User.id == id)
    results = db.exec(slq_delete)
    db.commit()
    return {"Usuario borrado con exito"}