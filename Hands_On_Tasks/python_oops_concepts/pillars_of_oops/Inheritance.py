'''Inheritance - child class which inherits the properties of parent class'''

class Books:
    
    def __init__(self, book_name, no_of_pages):
        self.book_name = book_name
        self.no_of_pages = no_of_pages
        
    def read(self):
        print(f"You can able to read the book : {self.book_name}\nIt has {self.no_of_pages} Pages")
        
class Story_Book(Books):
    
    def __init__(self, book_name, no_of_pages, author_name):
        # self.book_name = book_name
        # self.no_of_pages = no_of_pages
        super().__init__(book_name, no_of_pages)
        self.author_name = author_name
    
    def read(self):
        print(f"You can able to read the book : {self.book_name}\nIt has {self.no_of_pages} Pages\nThe book was written by : {self.author_name}")
      
class Director(Books, Story_Book):
    
    def __init__(self, book_name, no_of_pages, author_name,age):
        Story_Book.__init__(book_name, no_of_pages,author_name)
        self.age = age
    
    def read(self):
        print(f"You can able to read the book : {self.book_name}\nIt has {self.no_of_pages} Pages\nThe book was written by : {self.author_name}  age :{self.age}")  

# details  = Books("Harry Potter", 398)
details_1 = Director("PS4", 600, "Kirubakaran",23)
details_1.read()