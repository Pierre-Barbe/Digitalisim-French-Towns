from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Union, Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Commune(SQLModel, table=True):
    code_postal: Optional[int] = Field(default=None, primary_key=True)
    nom_commune: str = Field(index=True)
    departement: str


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/commune/")
def create_commune(commune: Commune):
    with Session(engine) as session:
        session.add(commune)
        session.commit()
        session.refresh(commune)
        return commune


@app.get("/commune/")
def read_commune():
    with Session(engine) as session:
        commune = session.exec(select(Commune)).all()
        return commune