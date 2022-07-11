from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from .. import models, schemas

"""
 Function : Get All Blog
"""
def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

"""
Function : Create Blog
"""

def create(request : schemas.Blog , db : Session):
    new_blog = models.Blog(title = request.title , body = request.body , user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

"""
Function : Delete Blog
"""

def delete(id : int ,db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"{id} Number blog is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog is Deleted"

"""
Function : Update Blog
"""

def put(id : int ,request : schemas.Blog , db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"{id} Number blog is not found")
    blog.update({'title' : request.title , 'body' : request.body})
    db.commit()
    return "Blog Was Updated Successfully!"

"""
Function : Get one blog Blog
"""

def get_one(id:int , db:Session):
    try:
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} Number blog is not available")
            # response.status_code = status.HTTP_404_NOT_FOUND
            # return {'details'  : f"{id} Number blog is not available"}
        print(blog)
        return blog
    except Exception as e:
        print(e)