from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from .. import models, schemas
from ..hashing import Hash

"""
Function : Create user
"""

def create_user(request : schemas.User , db : Session):
    new_user = models.User(name=request.name , email = request.email , password =Hash.bcrypy(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

"""
Function : Get user
"""

def get_user(id : int ,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"{id} This id user is not found!")

    return user