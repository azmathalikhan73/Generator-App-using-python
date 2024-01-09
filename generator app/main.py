import tkinter as tk
from tkinter import ttk
import random
from ttkthemes import ThemedTk

class GeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Generator App")
        self.root.geometry("300x200")

        # Use the 'plastik' theme for a modern look, feel free to experiment with other themes
        self.style = ttk.Style(root)
        self.style.theme_use("plastik")

        self.label = ttk.Label(root, text="Select a category:")
        self.label.pack(pady=10)

        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(root, textvariable=self.category_var, values=["Number", "Place", "Name", "Animal", "Sport"])
        self.category_combobox.pack(pady=10)

        self.min_var = tk.StringVar(value="1")
        self.max_var = tk.StringVar(value="100")

        self.min_label = ttk.Label(root, text="Min:")
        self.min_label.pack()
        self.min_entry = ttk.Entry(root, textvariable=self.min_var)
        self.min_entry.pack()

        self.max_label = ttk.Label(root, text="Max:")
        self.max_label.pack()
        self.max_entry = ttk.Entry(root, textvariable=self.max_var)
        self.max_entry.pack()

        self.generate_button = ttk.Button(root, text="Generate", command=self.generate_random)
        self.generate_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def generate_random(self):
        category = self.category_var.get()
        min_value = int(self.min_var.get())
        max_value = int(self.max_var.get())

        if min_value >= max_value:
            self.result_label.config(text="Min should be less than Max")
            return

        if category == "Number":
            result = str(random.randint(min_value, max_value))
        elif category == "Place":
            places = ["New York", "Paris", "Tokyo", "London", "Sydney"]
            result = random.choice(places)
        elif category == "Name":
            names = ["John", "Emma", "Michael", "Sophia", "William"]
            result = random.choice(names)
        elif category == "Animal":
            animals = ["Dog", "Cat", "Elephant", "Lion", "Giraffe"]
            result = random.choice(animals)
        elif category == "Sport":
            sports = ["Football", "Basketball", "Tennis", "Soccer", "Golf"]
            result = random.choice(sports)
        else:
            result = "Select a valid category"

        self.result_label.config(text=result)

if __name__ == "__main__":
    root = ThemedTk(theme="plastik")  # Create a themed Tkinter window
    app = GeneratorApp(root)
    root.mainloop()
