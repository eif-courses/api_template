from typing import List

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select

from data.database import create_db_and_tables, engine
from data.models import Document

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/api/documents", response_model=List[Document])
async def list_documents():
    with Session(engine) as session:
        documents = session.exec(select(Document)).all()
        return documents


@app.post("/api/documents")
async def create_document(doc: Document):
    with Session(engine) as session:
        session.add(doc)
        session.commit()
        session.refresh(doc)
        return doc


@app.get("/api/documents/{id}", response_model=Document)
async def read_document(doc_id: int):
    with Session(engine) as session:
        doc = session.get(Document, doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found!")
        return doc
