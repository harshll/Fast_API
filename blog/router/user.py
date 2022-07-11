from fastapi import APIRouter , Depends
from .. import schemas
from .. import database
from  typing import List
from sqlalchemy.orm import Session
from ..repository import user

"""
router = Instance of APIRouter
"""

router = APIRouter(
    prefix="/user" ,
    tags=['user']
)


get_db = database.get_db




"""
User block 
"""

# Create user

@router.post('/' , response_model = schemas.ShowUser)
def create_user(request : schemas.User,db : Session = Depends(get_db)):
    return user.create_user(request , db)

# Get user

@router.get('/{id}' , response_model=schemas.ShowUser)
def get_user(id : int , db : Session = Depends(get_db)):
    return user.get_user(id ,db)