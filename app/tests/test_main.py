from ..main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"data": "Hello World"}
    
def test_read_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    
def test_read_error():
    response = client.get("/error")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

