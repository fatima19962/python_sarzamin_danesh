import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3

class ProductApp:

    
    def update_product(self):
        if not self.selected_product_id:
            messagebox.showwarning("selection error","no product loaded fo update")
            return
        try:
            name=self.name_entry.get()
            price=float(self.price_entry.get())
            quantity=int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("invalid input","price must be a number and quantity must be an integer")
            return
        if not name:
            messagebox.showwarning("input error","name cannot be empty")
            return
        update_product_in_db(self.selected_product_id,name,price,quantity)
        self.clear_entries()
        self.load_products()


if __name__=="__main__":
    ProductApp()