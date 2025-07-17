from fastapi import APIRouter, Depends

from learnage.schemas.note import Note, NoteCreate
from learnage.services.notes import NoteService, get_note_service

router = APIRouter()


@router.post("/notes/", response_model=Note)
def create_note(
    note: NoteCreate,
    service: NoteService = Depends(get_note_service),
):
    return service.create_note(note=note)


@router.get("/notes/", response_model=list[Note])
def read_notes(
    skip: int = 0,
    limit: int = 10,
    service: NoteService = Depends(get_note_service),
):
    return service.get_notes(skip=skip, limit=limit)
