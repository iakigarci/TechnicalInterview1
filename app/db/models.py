from doctest import master
from sqlalchemy import Column, Integer, String
from .postgres import Base

class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    amount = Column(Integer)
    price = Column(Integer)
    material = Column(String)    
