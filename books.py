class User:
    def __init__(self, bookList: list) -> None:
        self.bookList = bookList

    def borrow(self, bookName:str):
        self.bookName = bookName
        for x in self.bookList:
            if (self.bookName in self.bookList):
                self.bookList.remove(self.bookName)
                break
            else:
                print(f"The book {self.bookName} is not avaible")
    
    def returns(self, bookName: str):
        self.bookName = bookName
        self.bookList.append(self.bookName)

    def avaible(self):
        return print(f"The books that are avaible are: {self.bookList}")
                

class librarian:
    def __init__(self, bookList: list) -> None:
        self.bookList = bookList

    def search(self, bookName:str): 
        self.bookName = bookName
        for x in bookName:
            if (self.bookName in self.bookList):
                print(f"The book {bookName} is avaible")
                break
            else:
                print(f"The book {bookName} is not avaible")


    def updateList(self, newBookList: list):
        pass
