from fastapi import FastAPI 
from . import  models 
from .database import  engine
from .router import blog,user,auth

"""
app = create instance of FastApi 
"""

app = FastAPI()

models.Base.metadata.create_all(engine)


"""
Auth Router
"""

app.include_router(auth.router)


"""
Blog Router
"""
app.include_router(blog.router)


"""
User Router
"""

app.include_router(user.router)





