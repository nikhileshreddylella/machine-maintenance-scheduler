from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
from database import SessionLocal
import models

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/maintenance/{task_id}")
def update_maintenance(
        task_id: int = Path(...),
        status: str = "",
        db: Session = Depends(get_db)
):

    task = db.query(models.Maintenance).filter(
        models.Maintenance.id == task_id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = status

    db.commit()
    db.refresh(task)

    return {"message": "Maintenance updated successfully"}