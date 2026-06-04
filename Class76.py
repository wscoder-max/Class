import tkinter as tk
from tkinter import ttk, messagebox
import os

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "Fries": 2,
            "Lunch": 2,
            "Burger": 3,
            "Pizza": 4,
            "Cheeseburger": 2.50,
            "Drink": 1
        }

        self.exchange_rates = {
            "GBP": 1.0,
            "USD": 1.25,
            "EUR": 1.18
        }

        self.currency_symbols = {
            "GBP": "£",
            "USD": "$",
            "EUR": "€"
        }

        self.setup_background(root)

        frame = ttk.Frame(root, padding = "20")
        frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        ttk.Label(frame, text = "Restaurant Order Management", font = ("Arial", 20, "bold")).grid(row = 0, columnspan = 2, padx = 10, pady = 10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start = 1):
            label = ttk.Label(frame, text = f"{item} (£{price:.2f}):", font = ("Arial", 12))
            label.grid(row = i, column = 0, padx = 10, pady = 5, sticky = "e")
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width = 5)
            quantity_entry.grid(row = i, column = 1, padx = 10, pady = 5, sticky = "w")
            quantity_entry.insert(0, "0") 
            self.menu_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(frame, text = "Currency:", font = ("Arial", 12)).grid(row = len(self.menu_items) + 1, column = 0, padx = 10, pady = 5, sticky = "e")

        currency_dropdown = ttk.Combobox(frame, textvariable = self.currency_var, state = "readonly", width = 10, values = ("GBP", "USD", "EUR"))
        currency_dropdown.grid(row = len(self.menu_items) + 1, column = 1, padx = 10, pady = 5, sticky = "w")
        currency_dropdown.current(0)
        self.currency_var.trace_add("write", self.update_menu_prices)

        order_button = ttk.Button(frame, text = "Place Order", command = self.place_order)
        order_button.grid(row = len(self.menu_items) + 2, columnspan = 2, padx = 10, pady = 15)

    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        
        if os.path.exists("background.png"):
            canvas = tk.Canvas(root, width = bg_width, height = bg_height)
            canvas.pack(fill = "both", expand = True)

            original_image = tk.PhotoImage(file = "background.png")
            sub_x = max(1, original_image.width() // bg_width)
            sub_y = max(1, original_image.height() // bg_height)
            background_image = original_image.subsample(sub_x, sub_y)

            canvas.create_image(0, 0, anchor = tk.NW, image = background_image)
            canvas.image = background_image
        else:
            root.configure(bg = "#f0f0f0")

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = self.currency_symbols[currency]
        rate = self.exchange_rates[currency]

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text = f"{item} ({symbol}{price:.2f}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n" + "-" * 20 + "\n"
        currency = self.currency_var.get()
        symbol = self.currency_symbols[currency]
        rate = self.exchange_rates[currency]

        for item, entry in self.menu_quantities.items():
            quantity = entry.get().strip()
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    price = self.menu_items[item] * rate
                    cost = quantity * price
                    total_cost += cost
                    order_summary += f"{item}: {quantity} x {symbol}{price:.2f} = {symbol}{cost:.2f}\n"

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed!", order_summary)
        else:
            messagebox.showerror("Error", "Please enter a valid quantity greater than 0 for at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = RestaurantOrderManagement(root)
    root.mainloop()