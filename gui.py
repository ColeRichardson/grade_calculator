import tkinter as tk

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UTM Grade Calculator")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(background='black')
        self.widgets = []

        for i in range(5):
            tk.Label(self.root, text='Assessment Name', background='white', padx=10, pady=10).grid(row=i)

        for i in range(5):
            tk.Entry(self.root, bg='orange').grid(row=i, column=1)

        for i in range(5):
            tk.Label(self.root, text='Weight', background='white', padx=10, pady=10).grid(row=i, column=2)

        for i in range(5):
            tk.Entry(self.root, bg='orange').grid(row=i, column=3)

        for i in range(5):
            tk.Label(self.root, text='Grade %', background='white', padx=10, pady=10).grid(row=i, column=4)

        for i in range(5):
            tk.Entry(self.root, bg='orange', justify='center').grid(row=i, column=5)

        self.root.mainloop()

    def addField(self):
        pass

    def delField(self):
        pass

    
