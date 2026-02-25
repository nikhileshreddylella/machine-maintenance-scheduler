from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class MachineCreate(BaseModel):
    id: int
    name: str
    type: str
    status: str


@app.get("/")
def home():
    return {"message": "Machine Service Running"}



@app.post("/machines")
def add_machine(machine: MachineCreate, db: Session = Depends(get_db)):
    new_machine = models.Machine(
        id=machine.id,
        name=machine.name,
        type=machine.type,
        status=machine.status
    )

    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)

    return {"message": "Machine stored in database"}



@app.get("/machines")
def get_machines(db: Session = Depends(get_db)):
    machines = db.query(models.Machine).all()
    return machines
