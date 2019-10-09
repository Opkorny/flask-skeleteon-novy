from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime

from ..database import db
from ..mixins import CRUDModel

class Vozidlo(CRUDModel):
    __tablename__ = 'vozidlo'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer,primary_key=True)
    typ = Column(String,nullable=False,index=True)
    spz = Column(String,nullable=False,index=True,unique=True)