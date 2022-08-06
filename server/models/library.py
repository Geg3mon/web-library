from __future__ import annotations


class Book:
    title: str = None  # Book title
    genre: str = None  # Book genre
    author: str = None  # Book author

    def __init__(self, genre: str, title: str, author: str):
        self.genre = genre
        self.title = title
        self.author = author

    def __str__(self):
        return f'{{ "Title": "{self.title}", "Genre": "{self.genre}", "Author": "{self.author}" }}'

    def __eq__(self, other):
        return (self.genre == other.genre and
                self.title == other.title and
                self.author == other.author)


class Reader:
    booksy: list[Book] = []  # List of books at readers
    full_name: str = None  # First name and last name of reader
    number: str = None  # Unique reader ID at self.library
    birthday: str = None  # Birthday date of reader
    phone: str = None  # Reader phone number
    status: bool = True  # Reader status

    def __init__(self, full_name: str, number: str, birthday: str, phone: str,
                 status=True):
        self.full_name = full_name
        self.number = number
        self.birthday = birthday
        self.phone = phone
        self.status = status

    def __eq__(self, other):
        return self.number == other.number

    def __str__(self):
        return f'Full name: {self.full_name}, Number ID: {self.number}'


class Library():

    library_numbers: list = []  # List of unique readers ID numbers
    library_books: list[Book] = []  # Books in library
    readers_books: list[Book] = []  # Books at readers
    library_readers: list[Reader] = []  # Reader at self.library
    library_amount: int = 0  # Library amount
    book: Book = None  # Class with book object
    reader: Reader = None  # Class with book reader
    adress: str = None  # Library adress
    phone: str = None  # Library phone

    def __init__(self, adress: str, phone: str, books: list[Book],
                 readers: list[Reader]):
        self.adress = adress
        self.phone = phone
        self.books = books
        self.readers = readers
        self.library_books.extend(books)
        self.library_readers.extend(readers)

        for i in readers:
            if i.number in self.library_numbers:
                raise ValueError(f'User with number {i.number} already exist')
            else:
                self.library_numbers.append(i.number)

    def library_books_list(self):
        return f'{", ".join(map(str, self.library_books))}'

    def takeBook(self, book: Book, reader: Reader):
        if book in self.library_books and reader.status == True and reader in self.library_readers:
            self.readers_books.append(book)
            self.library_books.remove(book)
            reader.booksy.append(book)
            return f'{reader.full_name} take book {book.title}'
        elif reader.status == False:
            return f'{reader.full_name} must pay library fee'
        else:
            return f'There is no {book.title} in Library\n{book}\n{self.library_books}\n{self.library_readers}'

    def returnBook(self, book: Book, reader: Reader):
        reader.booksy.remove(book)
        self.library_books.append(book)
        return f'{reader.full_name} return book {book.title}'

    def whatRead(self):
        for readers in self.library_readers:
            if len(readers.booksy) > 0:
                return f'Readers have this books: {", ".join(map(str, readers.booksy))}\n'
        else:
            return f'At this moment all books in library'

    def addBook(self, book: Book):
        self.library_books.append(book)
        return f'You add new book: {book.title}'

    def deleteBook(self, book: Book):
        try:
            self.library_books.remove(book)
            return f'You remove book: {book.title}'
        except:
            pass

    def addReader(self, reader: Reader):
        if reader.number in self.library_numbers:
            raise ValueError(f'User with number {reader.number} already exist')
        else:
            self.library_numbers.append(reader.number)
            self.library_readers.append(reader)
            return f'You add new reader: {reader.full_name}'

    def deleteReader(self, reader: Reader):
        self.library_numbers.remove(reader.number)
        self.library_readers.remove(reader)
        return f'You remove reader: {reader.full_name}'

    def checkStatus(self, reader: Reader):
        if reader.status == True:
            return f'{reader.full_name} payed library fee and can take books'
        else:
            return f'{reader.full_name} must pay library fee'

    def payedFee(self, reader: Reader):
        if reader.status == False:
            self.library_amount += 10
            reader.status = True
            return f'{reader.full_name} pay library fee and can take books'
        else:
            return f'{reader.full_name} already payed library fee'

    def readerCount(self):
        return f'At this library {len(self.library_readers)} members'

    def __str__(self):
        return f'Books: {", ".join(map(str, self.library_books))}\nReaders: {", ".join(map(str, self.library_readers))}'

my_library = Library('Ukraine', '3700',
                     [
                         Book('1111', 'BOOK 1', '1'),
                         Book('2222', 'BOOK 2', '2')
                     ],
                     [
                     ])

# if __name__ == '__main__':
#     book1 = Book('1111', 'BOOK 1', '1')
#     book2 = Book('2222', 'BOOK 2', '2')
#     reader2 = Reader('Petro First One', '181456', '08.09.95', '5553535', True)
#     reader1 = Reader('Petro Second', '2814556', '1965', '32456', True)
#     a = Library('Baker st 221, B', '8800553535', [book1, book2], [reader1])
#     a.addReader(Reader('Ivan', '8814456', '08.09.95', '5553535'))
#     a.addBook(Book('Wiki', 'Wiki', 'Arsen'))
#     print(a.whatRead())
#     print(a.library_readers)
#     print(a.addReader(reader2))
#     print(a.library_books)
#     print(a.takeBook(book2, reader2) + "========")
#     print(a.whatRead())
#     print(reader1.booksy)
#     print(a.takeBook(book1, reader1) + '--------')
#     print(a.whatRead())
#     print(reader2.booksy)
#     print(a.library_books_list())
#     print(a.addBook(Book('Name','1','2')))
#     print(a.library_books_list())
