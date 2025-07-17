from sqlalchemy.orm import Session
from fastapi import Depends

from learnage.models.note import Note
from learnage.schemas.note import NoteCreate

from ..clients.database import get_db


class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_note(self, note: NoteCreate) -> Note:
        db_note = Note(title=note.title, content=note.content)
        self.db.add(db_note)
        self.db.commit()
        self.db.refresh(db_note)
        return db_note

    def get_notes(self, skip: int = 0, limit: int = 10) -> list[Note]:
        return self.db.query(Note).offset(skip).limit(limit).all()


def get_note_repository(db: Session = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db=db)
