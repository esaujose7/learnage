from fastapi import Depends

from learnage.schemas.note import NoteCreate
from ..repositories.notes import NoteRepository, get_note_repository


class NoteService:
    def __init__(self, repository: NoteRepository):
        self.repository = repository

    def create_note(self, note: NoteCreate):
        return self.repository.create_note(note=note)

    def get_notes(self, skip: int, limit: int):
        return self.repository.get_notes(skip=skip, limit=limit)


def get_note_service(
    repo: NoteRepository = Depends(get_note_repository),
) -> "NoteService":
    return NoteService(repository=repo)
