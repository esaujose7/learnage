from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from learnage import models
from learnage.clients.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notes/")
def create_note(title: str, content: str, db: Session = Depends(get_db)):
    db_note = models.Note(title=title, content=content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/notes/")
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notes = db.query(models.Note).offset(skip).limit(limit).all()
    return notes
