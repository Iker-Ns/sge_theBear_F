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
    return {"message": "Created user succesfully"}

def update_user(id:int,name:str, db:Session):
    sql_update = update(User).where(User.id == id).values(name=name)
    db.exec(sql_update)
    db.commit()
    return {"message": "Usuario actualizado con exito"}

def delete_user(id:int, db:Session):
    slq_delete = delete(User).where(User.id == id)
    db.exec(slq_delete)
    db.commit()
    return {"message":"Usuario borrado con exito"}