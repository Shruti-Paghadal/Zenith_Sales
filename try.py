import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('ORDER STATUS')
root.geometry('620x200')
columns = ('party_Name', 'model', 'finish','size','quantity','date_of_Order','status')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('party_Name', text='Party Name')
tree.heading('model', text='Model')
tree.heading('finish', text='Finish')
tree.heading('size', text='Size')
tree.heading('quantity', text='Quantity')
tree.heading('date_of_Order', text='Date of Order')
tree.heading('status', text='Status')

