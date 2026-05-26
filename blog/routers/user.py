from fastapi import FastAPI, Depends
from .. import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from ..repository import user 


router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)
get_db = database.get_db


@router.post('/', response_model = schemas.showUser)
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user.create_user(request,db)


@router.get('/{id}', response_model = schemas.showUser)
def get_user(id : int, db : Session = Depends(get_db)):
   return user.get_user(id, db)
