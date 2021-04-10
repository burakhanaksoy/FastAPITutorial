from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Blog(Base):
    __tablename__ = "Blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    user = Column(String, unique=True, index=True)
    likes = Column(Integer)
    published = Column(Boolean, default=False)