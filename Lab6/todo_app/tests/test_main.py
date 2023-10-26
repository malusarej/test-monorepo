import sys
sys.path.append(".")
from fastapi.testclient import TestClient
from src.main import app, books

client = TestClient(app)

def test_get_with_path_params():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json() == {"msg": "1"}

def test_get_with_query_params():
    response = client.get("/books/?title=Book1")
    assert response.status_code == 200
    assert response.json() == {"msg": "Book1"}

def test_post():
    response = client.post("/books/create_book", json={"new_book": "Book3"})
    assert response.status_code == 200
    assert response.json() == {"msg": {"new_book": "Book3"}}

def test_put_with_path_params():
    response = client.put("/books/1?title=NewTitle")
    assert response.status_code == 200
    assert response.json() == {"author": "RF Kuang", "title": "NewTitle", "category": "Fantasy"}

def test_put_nonexistent_book():
    # Attempt to update a book that doesn't exist (e.g., book ID 99)
    response = client.put("/books/99?title=NewTitle")
    assert response.status_code == 200
    assert response.json() == {"error": "Book not found"}

def test_delete_with_path_params():
    # Add a book to the simulated data
    books[1] = {"title": "Book1", "author": "Author1"}

    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Book with ID 1 has been deleted", "deleted_book": {"title": "Book1", "author": "Author1"}}
