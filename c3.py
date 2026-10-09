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
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Product Management")

        self.selected_product_id = None

        self.create_widgets()
        self.load_products()

        self.root.mainloop()

    def create_widgets(self):
        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Price:").grid(row=0, column=2, padx=5)
        self.price_entry = tk.Entry(input_frame)
        self.price_entry.grid(row=0, column=3, padx=5)

        tk.Label(input_frame, text="Quantity:").grid(row=0, column=4, padx=5)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=0, column=5, padx=5)

        tk.Button(input_frame, text="Add Product", command=self.add_product).grid(row=0, column=6, padx=5)

        # Search Frame
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="Search:").grid(row=0, column=0, padx=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_products).grid(row=0, column=2, padx=5)
        tk.Button(search_frame, text="Show All", command=self.load_products).grid(row=0, column=3, padx=5)

        # Treeview
        tree_frame = tk.Frame(self.root)
        tree_frame.pack(pady=10)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Price", "Quantity"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.pack()

        # Action Buttons
        action_frame = tk.Frame(self.root)
        action_frame.pack(pady=10)

        tk.Button(action_frame, text="Load for Edit", command=self.load_selected_product).grid(row=0, column=0, padx=5)
        tk.Button(action_frame, text="Update Product", command=self.update_product).grid(row=0, column=1, padx=5)
        tk.Button(action_frame, text="Delete Product", command=self.delete_product).grid(row=0, column=2, padx=5)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.selected_product_id = None

    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for product in get_all_products():
            self.tree.insert('', 'end', values=product)

    def add_product(self):
        name = self.name_entry.get()
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Price must be a number and Quantity must be an integer.")
            return

        if not name:
            messagebox.showwarning("Input Error", "Name cannot be empty.")
            return

        add_product_to_db(name, price, quantity)
        self.clear_entries()
        self.load_products()

    def search_products(self):
        search_term = self.search_entry.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for product in search_products_in_db(search_term):
            self.tree.insert('', 'end', values=product)

    def delete_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "No product selected.")
            return
        product_id = self.tree.item(selected)['values'][0]
        delete_product_from_db(product_id)
        self.load_products()

    def load_selected_product(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "No product selected.")
            return
        product = self.tree.item(selected)['values']
        self.selected_product_id = product[0]
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, product[1])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, product[2])
        self.quantity_entry.delete(0, tk.END)
        self.quantity_entry.insert(0, product[3])

    def update_product(self):
        if not self.selected_product_id:
            messagebox.showwarning("Selection Error", "No product loaded for update.")
            return
        try:
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Price must be a number and Quantity must be an integer.")
            return
        if not name:
            messagebox.showwarning("Input Error", "Name cannot be empty.")
            return

        update_product_in_db(self.selected_product_id, name, price, quantity)
        self.clear_entries()
        self.load_products()

# ===================== Run App =====================
if __name__ == "__main__":
    ProductApp()
