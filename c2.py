import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ===================== Database Functions =====================

def connect_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity INTEGER
        )
    ''')
    conn.commit()
    return conn, cursor

def add_product_to_db(name, price, quantity):
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
                   (name, price, quantity))
    conn.commit()
    conn.close()

def get_all_products():
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

def search_products_in_db(search_term):
    conn, cursor = connect_db()
    cursor.execute('''
        SELECT * FROM products 
        WHERE name LIKE ? 
        OR CAST(quantity AS TEXT) LIKE ? 
        OR CAST(price AS TEXT) LIKE ?
    ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    products = cursor.fetchall()
    conn.close()
    return products

def delete_product_from_db(product_id):
    conn, cursor = connect_db()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

def update_product_in_db(product_id, name, price, quantity):
    conn, cursor = connect_db()
    cursor.execute('UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?',
                   (name, price, quantity, product_id))
    conn.commit()
    conn.close()

# ===================== GUI Class =====================

class ProductApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")
        
        self.selected_product_id = None  # Store selected product ID
        
        self.create_widgets()
        self.show_products()

    def create_widgets(self):
        # Input fields
        ttk.Label(self.root, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Price:").grid(row=1, column=0, sticky="w")
        self.price_entry = ttk.Entry(self.root)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="Quantity:").grid(row=2, column=0, sticky="w")
        self.quantity_entry = ttk.Entry(self.root)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        ttk.Button(self.root, text="Add Product", command=self.add_product).grid(row=3, column=0, pady=5)
        ttk.Button(self.root, text="Show Products", command=self.show_products).grid(row=3, column=1, pady=5)
        ttk.Button(self.root, text="Edit Product", command=self.load_selected_product).grid(row=3, column=2, pady=5)

        # Search
        ttk.Label(self.root, text="Search:").grid(row=4, column=0, sticky="w")
        self.search_entry = ttk.Entry(self.root)
        self.search_entry.grid(row=4, column=1, padx=5, pady=5)
        ttk.Button(self.root, text="Search", command=self.search_product).grid(row=4, column=2, padx=5)

        # Treeview for products
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Price", "Quantity"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.selected_product_id = None

    def add_product(self):
        try:
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            if not name:
                messagebox.showwarning("Input Error", "Name cannot be empty.")
                return

            add_product_to_db(name, price, quantity)
            self.clear_entries()
            self.show_products()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

    def show_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for product in get_all_products():
            self.tree.insert("", tk.END, values=product)

    def search_product(self):
        search_term = self.search_entry.get()
        results = search_products_in_db(search_term)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for product in results:
            self.tree.insert("", tk.END, values=product)

        if not results:
            messagebox.showinfo("Search Results", "No products found.")

    def load_selected_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a product to edit.")
            return
        
        product = self.tree.item(selected[0], "values")
        self.selected_product_id = product[0]  # Store ID
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, product[1])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, product[2])
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, product[3])

        # Change button text to "Update"
        ttk.Button(self.root, text="Update Product", command=self.update_product).grid(row=3, column=3, pady=5)

    def update_product(self):
        if self.selected_product_id is None:
            messagebox.showerror("Error", "No product selected for update.")
            return

        try:
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            update_product_in_db(self.selected_product_id, name, price, quantity)
            messagebox.showinfo("Success", "Product updated successfully!")
            self.clear_entries()
            self.show_products()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

# ===================== Main Program =====================

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductApp(root)
    root.mainloop()
