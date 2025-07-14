from fastapi import FastAPI
from learnage.api import notes

app = FastAPI()

app.include_router(notes.router)