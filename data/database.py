from sqlmodel import SQLModel, create_engine

database_name = "documents.sqlite"
url = f"sqlite:///{database_name}"
engine = create_engine(url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
