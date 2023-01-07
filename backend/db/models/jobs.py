from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base


class Job(Base):
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    company = Column(String,nullable=False)
    company_url = Column(String) #By default nullable=True means it can be null
    location = Column(String,nullable=False)
    description =Column(String,nullable=False)
    date_posted = Column(String)
    is_active = Column(Boolean(),default=True) # columns will be used to control if the job post will be visible on the website
    owner_id = Column(Integer,ForeignKey('user.id'),) # this defines the relationship in the database
    owner = relationship("User",back_populates="jobs",) # this defines the relationship in the python code or ORM Layer
