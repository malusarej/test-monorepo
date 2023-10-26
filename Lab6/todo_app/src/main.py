from fastapi import FastAPI, Body

app = FastAPI()

#dummy data
books = {
    1: {"title": "Poppy War", "author": "RF Kuang", "category": "Fantasy"},
    2: {"title": "Vicious", "author": "VE Schwab", "category": "Dystopia"},
}

#Create a GET ReST API
@app.get("/api")
def first_api():
    return{"msg":"hello world"}

#Create a GET ReST API with path parameters
@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return{"msg": path_param}

#Create a GET ReST API with query parameters
@app.get("/books/")
def first_apiV3(title: str):
    return{"msg": title}

#Create a POST ReST API
@app.post("/books/create_book")
def first_apiV4(new_book = Body()):
    print(new_book)
    return {"msg": new_book}

#Create a GET ReST API with path parameters AND query parameters
@app.get("/books/{book_id}")
def get_book(book_id: int, category: str):
    return {"book_id": book_id, "category": category}

#Create a PUT ReST API
@app.put("/books/{book_id}")
def update_book(book_id: int, title: str = None, author: str = None, category: str = None):
    if book_id in books:
        if title:
            books[book_id]["title"] = title
        if author:
            books[book_id]["author"] = author
        if category:
            books[book_id]["category"] = category
        return books[book_id]
    else:
        return {"error": "Book not found"}

#Create a DELETE ReST API    
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id in books:
        deleted_book = books.pop(book_id)
        return {"message": f"Book with ID {book_id} has been deleted", "deleted_book": deleted_book}
    else:
        return {"error": "Book not found"}
