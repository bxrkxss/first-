class Book: 
    def __init__( self, title, author, number_of_pages=0 ):
        self.title = title 
        self.author = author 
        self.number_of_pages = number_of_pages
        
    def describe(self):
        print("Book author: " + self.author)
        print("Book title: " + self.title)
        
    def is_long(self):
        if self.number_of_pages > 200:
            return True 
        else:
            return False
        
my_book = Book("tetovaya", "zopa, 201")

my_book.describe()
print(my_book.is_long())
