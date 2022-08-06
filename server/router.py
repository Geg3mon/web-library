from __future__ import annotations
from models.library import my_library, Book, Reader


routes = [
    {
        "method": "GET",
        "path": "/v1/library/books",
        "call": my_library.library_books_list()
    },
    {
        "method": "POST",
        "path": "/v1/library/add/book",
        "call": my_library.addBook(Book('Name','Name','2'))
    },
    {
        "method": "DELETE",
        "path": "/v1/library/del/book",
        "call": my_library.deleteBook(Book('','',''))
    },
]
