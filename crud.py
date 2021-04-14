from sqlalchemy.orm import Session
from models import UserModel
from schemas import User

def list_user(db: Session): #Faltou a paginação
    return db.query(UserModel).all()

def store_user(db: Session, newUser: User):
    user_to_db = UserModel(**newUser.dict())
    db.add(user_to_db)
    db.commit()
    db.refresh(user_to_db)
    return user_to_db