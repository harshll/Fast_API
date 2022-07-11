from sqlalchemy import Column, ForeignKey,Integer,String
from .database import Base
from sqlalchemy.orm import relationship


# Blog model
class Blog(Base):

    __tablename__ = 'blogs'

    id = Column(Integer , primary_key = True , index =True)
    title= Column(String)
    body = Column(String)
    user_id = Column(Integer , ForeignKey('user.id'))

    # For Get creator 
    creator = relationship("User" , back_populates = "blogs")

# User model

class User(Base):

    __tablename__ = 'user'

    id = Column(Integer , primary_key = True , index =True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    
    # For Get Blogs
    blogs = relationship("Blog" , back_populates = "creator")

