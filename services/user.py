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

def update_existing_user(search_name:str, new_name:str, email:str, db:Session):
    user = db.exec(select(User).where(User.name == search_name)).one()
    user.name = new_name
    user.email = email
    db.add(user)
    db.commit()
    return {"message": "User updated", "user": {
        "name": user.name,
        "email": user.email
    }}

def delete_user(name:str, db:Session):
    user = db.exec(select(User).where(User.name == name)).one()
    db.delete(user)
    db.commit()
    return {"message": "User deleted succesfully"}