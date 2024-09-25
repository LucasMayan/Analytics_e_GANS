import tkinter as tk
from tkinter import messagebox
import random

class BookStoreInventory:
    def __init__(self):
        self.inventory = {
            "Sapiens: Uma breve história da humanidade": 5,
            "Duna": 3,
            "O Hobbit": 2,
            "O Senhor dos Anéis": 4,
            "O Código Da Vinci": 2,
            "Orgulho e Preconceito": 3,
            "O Último Guardião": 1,
            "A Garota no Trem": 2,
        }
    
    def addBook(self, title, quantity):
        if title in self.inventory:
            self.inventory[title] += quantity
        else:
            self.inventory[title] = quantity

    def checkQuantity(self, title):
        return self.inventory.get(title, 0)
    
    def removeBook(self, title, quantity):
        if title in self.inventory and self.inventory[title] >= quantity:
            self.inventory[title] -= quantity
            if self.inventory[title] == 0:
                del self.inventory[title]
            return True
        return False
    
    def recommendBooks(self, description):
        keywords = description.lower().split()
        recommendations = {
            'análise': 'Os elementos',
            'aventura': 'O Hobbit',
            'fantasia': 'O Senhor dos Anéis',
            'história': 'Sapiens: Uma breve história da humanidade',
            'sci-fi': 'Duna',
            'mistério': 'O Código Da Vinci',
            'romance': 'Orgulho e Preconceito',
            'ação': 'O Último Guardião',
            'thriller': 'A Garota no Trem'
        }
        
        # Primeiro, verifica se há uma recomendação com base nas palavras-chave
        for keyword in keywords:
            if keyword in recommendations:
                return recommendations[keyword]

        # Se nenhuma recomendação foi encontrada, sugere um livro aleatório do inventário
        if self.inventory:
            random_book = random.choice(list(self.inventory.keys()))
            return f"Recomendamos: {random_book}"
        
        return 'O inventário está vazio. Sem recomendações disponíveis.'

    def getInventory(self):
        return self.inventory

class BookStoreApp:
    def __init__(self, root):
        self.bookstore = BookStoreInventory()
        
        self.root = root
        self.root.title("Gerenciador de Inventário de Livraria")
        
        # Adicionar Livro
        self.title_label = tk.Label(root, text="Título do Livro:")
        self.title_label.pack()
        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantidade:")
        self.quantity_label.pack()
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.add_button = tk.Button(root, text="Adicionar Livro", command=self.add_book)
        self.add_button.pack()

        # Remover Livro
        self.remove_button = tk.Button(root, text="Remover Livro", command=self.remove_book)
        self.remove_button.pack()

        # Verificar Inventário
        self.check_inventory_button = tk.Button(root, text="Verificar Inventário", command=self.check_inventory)
        self.check_inventory_button.pack()

        # Recomendar Livro
        self.desc_label = tk.Label(root, text="Descrição para Recomendação:")
        self.desc_label.pack()
        self.desc_entry = tk.Entry(root)
        self.desc_entry.pack()

        self.recommend_button = tk.Button(root, text="Obter Recomendação", command=self.recommend_book)
        self.recommend_button.pack()

    def add_book(self):
        title = self.title_entry.get()
        quantity = self.quantity_entry.get()

        if title and quantity.isdigit():
            self.bookstore.addBook(title, int(quantity))
            messagebox.showinfo("Sucesso", f"Livro '{title}' adicionado com quantidade {quantity}.")
            self.title_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Título e quantidade devem ser válidos.")

    def remove_book(self):
        title = self.title_entry.get()
        quantity = self.quantity_entry.get()

        if title and quantity.isdigit():
            if self.bookstore.removeBook(title, int(quantity)):
                messagebox.showinfo("Sucesso", f"Livro '{title}' removido com quantidade {quantity}.")
            else:
                messagebox.showerror("Erro", "Quantidade insuficiente ou livro não encontrado.")
            self.title_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Título e quantidade devem ser válidos.")

    def check_inventory(self):
        inventory = self.bookstore.getInventory()
        if inventory:
            inventory_list = "\n".join(f"{title}: {quantity}" for title, quantity in inventory.items())
            messagebox.showinfo("Inventário", f"Livros presentes:\n{inventory_list}")
        else:
            messagebox.showinfo("Inventário", "O inventário está vazio.")

    def recommend_book(self):
        description = self.desc_entry.get()
        recommendation = self.bookstore.recommendBooks(description)
        messagebox.showinfo("Recomendação", recommendation)
        self.desc_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookStoreApp(root)
    root.mainloop()