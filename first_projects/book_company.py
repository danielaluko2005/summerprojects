
class BooksAvailable:
    all_books=set()

    def __init__(self,book_name):
        self.book_name=book_name
        # self.books=all_books
        BooksAvailable.all_books.add(self.book_name)
    @classmethod
    def add_books_and_price(cls):
        return BooksAvailable.all_books
        # BooksAvailable.all_books=set()
        # book_to_add=input("Enter the book you wan't to add::-- ")
        # BooksAvailable.all_books.add(book_to_add)
        # return 
x=BooksAvailable("ronaldo")
print(x.add_books_and_price())
y=BooksAvailable("Messi")

print(y.add_books_and_price())
# print(BooksAvailable.add_books_and_price())
# print(BooksAvailable.add_books_and_price())