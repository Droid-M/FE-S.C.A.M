from fastapi import FastAPI, Depends
from schemas import User
from models import UserModel, Base
from crud import list_user, store_user
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

Base.metadata.create_all(bind=engine)
app = FastAPI()

#Abrindo conexão com o banco:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/") #Raiz
def root():
    return "Tela inicial *Use sua imaginação*"


@app.get("/lista-usuarios") #Lista usuários
async def get_all_users(db: Session = Depends(get_db)):
    return list_user(db)

@app.post("/cadastro-usuario", response_model = User) #Cadastra usuário
async def create_user(user: User, db: Session = Depends(get_db)):
    user = store_user(db, user)
    if(user is not None):
        return "Usuário criado com sucesso \nNome: " + user.name + "\nCPF" + user.cpf
    return "Falha ao registrar usuário"
