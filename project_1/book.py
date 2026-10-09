class Book:
    def __init__(self,book_id,name,price,stock):
        self.book_id=book_id
        self.name=name
        self.price=price
        self.stock=stock
    def __str__(self):
        return f"Book ID: {self.book_id}, Name: {self.name}, Price: {self.price}, Stock: {self.stock}"