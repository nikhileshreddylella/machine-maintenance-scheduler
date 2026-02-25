from sqlalchemy import Column, Integer, String, Date
from database import Base

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    status = Column(String)


class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(Integer)
    scheduled_date = Column(Date)
    technician = Column(String)
    status = Column(String)