class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.history=[]

    def buy_book(self, book):
        if book.stock > 0:
            book.stock -= 1
            self.history.append(book.name)
            return True
        return False