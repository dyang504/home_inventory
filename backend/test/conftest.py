import pytest
from typing import Any, Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.db.database import Base, get_db
from backend.main import app

SQL_DB_URL = "sqlite:///./test.db"

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def test_app():
    Base.metadata.create_all(bind=engine)
    _app = app
    yield _app
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(test_app: FastAPI):
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    yield session
    transaction.rollback()
    connection.close()


@pytest.fixture
def client(test_app, db_session):
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    test_app.dependency_overrides[get_db] = _get_test_db
    with TestClient(test_app) as client:
        yield client
