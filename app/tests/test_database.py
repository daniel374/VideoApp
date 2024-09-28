import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.database import get_db, Base
from app.main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


client = TestClient(app)
app.dependency_overrides[get_db] = override_get_db


def test_create_user():
    # Datos de prueba para un nuevo usuario
    user_data = {"name_usr": "Test User", "email_usr": "test@example.com"}

    # Enviar un POST para crear un nuevo usuario
    response = client.post("/users/", json=user_data)
    print(response.json())
    assert response.status_code == 200
    # Verificar que el código de estado sea 200
    assert response.status_code == 200
    # Obtener la respuesta JSON
    response_data = response.json()
    # Verificar que el ID del usuario se haya generado
    assert "id_usr" in response_data

    # Verificar que el nombre y el email coincidan con los datos enviados
    assert response_data["name_usr"] == user_data["name_usr"]
    assert response_data["email_usr"] == user_data["email_usr"]


# Prueba para verificar que se puedan obtener usuarios
def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0


