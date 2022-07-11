from fastapi import APIRouter , Depends, status

from blog.router.oauth2 import get_current_user
from .. import schemas
from .. import database
from  typing import List
from sqlalchemy.orm import Session
from ..repository import blog

"""
router = Instance of APIRouter
"""
router = APIRouter(
    prefix= "/blog",
    tags=['blogs']
)

# Get data for database
get_db = database.get_db



"""
get = Get perticuler blog from database
"""

@router.get('/{id}' , status_code=status.HTTP_200_OK , response_model=schemas.ShowBlog)
def show(id:int , db : Session = Depends(get_db) ,current_user : schemas.User = Depends(get_current_user) ):
    return blog.get_one(id,db)



"""
get = all blogs from database
"""

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(get_db) , current_user : schemas.User = Depends(get_current_user)):
    return blog.get_all(db)
    # blogs = db.query(models.Blog).all()
    # print(blogs)
    # return blogs



"""
Post = Create New blog
"""

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request :schemas.Blog,db : Session = Depends(get_db) ,current_user : schemas.User = Depends(get_current_user)):
    return blog.create(request , db)



"""
Delete = Delete blog from database
"""
@router.delete('/{id}' , status_code=status.HTTP_204_NO_CONTENT )
def destroy(id : int , db : Session = Depends (get_db) , current_user : schemas.User = Depends(get_current_user)):
    return blog.delete(id , db)


"""
Put = Update blog from database
"""
@router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Blog ,db : Session = Depends(get_db), current_user : schemas.User = Depends(get_current_user)):
    return blog.put(id,request,db)




