#----------------------------------------------------------------------------------
# Question 1
# Create a class BookStore.
# Instance variables: Name, Author
# Class variable: NoOfBooks = 0
# Constructor accepts Name and Author and increments NoOfBooks by 1.
# Display() - Display book details in the format:
# <BookName> by <Author>. No of books: <NoOfBooks>
# Create multiple objects and call Display().
#------------------------------------------------------------------------------------

class BookStore():
    
    NoOfBook = 0
    
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBook += 1
        
    def Display(self):
        print(self.Name, "by", self.Author + ".", "No of books:", BookStore.NoOfBook)
        
        
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()        
        
    