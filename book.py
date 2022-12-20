class Publisher:
    def getpublisher(self):
        self.name=input("enter the name of the publisher")

    def display(self):
        print("The Publisher of the book is",self.name)

class Book(Publisher):
    def getbook(self):
        self.title=input("enter the title of the book")
        self.author=input("enter the name of the author")

    def display1(self):
        print("Title Of The Book",self.title)
        print("Author Name",self.author)

class Python(Book):
    def bookdetails(self):
        self.price=int(input("Enter the price"))
        self.pages=int(input("Enter number of pages"))

    def display2(self):

        print(" Price Of The Book ",self.price)
        print(" Number Of Pages ",self.pages)


obj1=Python()
obj1.getpublisher()
obj1.getbook()
obj1.bookdetails()
obj1.display()
obj1.display1()
obj1.display2()