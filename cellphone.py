class cellphone:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def display_info(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Price: ${self.__price}"
    
