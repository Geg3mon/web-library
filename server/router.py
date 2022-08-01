from models.library import my_library

routes = [
    {
        "method": "GET",
        "path": "/v1/library/books",
        "call": my_library.library_books_list()
    },
    {
        "method": "POST",
        "path": "/v1/library/add/book",
        "call": my_library.addBook()
    },
    {
        "method": "DELETE",
        "path": "/v1/library/del/book",
        "call": my_library.deleteBook()
    },
]