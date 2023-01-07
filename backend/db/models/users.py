from sqlalchemy import Column, Integer, Boolean, ForeignKey,String
from sqlalchemy.orm import relationship
from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False) # means it can't be null
    email = Column(String, unique=True,index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner")
    
    