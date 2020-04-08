import tkinter as tk

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UTM Grade Calculator")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(background='black')
        self.num = 5
        self.widgets = []
        self.marks = []
        self.weights = []

        for i in range(self.num):
            tk.Label(self.root, text='Assessment Name', background='white', padx=10, pady=10).grid(row=i)

        for i in range(self.num):
            tk.Entry(self.root, bg='orange').grid(row=i, column=1)

        for i in range(self.num):
            tk.Label(self.root, text='Weight %', background='white', padx=10, pady=10).grid(row=i, column=2)

        for i in range(self.num):
            weight = tk.Entry(self.root, bg='orange')
            weight.grid(row=i, column=3)
            print(type(weight))
            self.weights.append(weight)
        for i in range(self.num):
            tk.Label(self.root, text='Grade %', background='white', padx=10, pady=10).grid(row=i, column=4)

        for i in range(self.num):
            mark = tk.Entry(self.root, bg='orange', justify='center')
            mark.grid(row=i, column=5)
            print(type(mark))
            self.marks.append(mark)

        tk.Button(text="calculate average", command=self.get_avg).grid(row=self.num+1, column=1)
        self.root.mainloop()

    def addField(self):
        pass

    def delField(self):
        pass

    def create_print_text(self, avg, weightt):
        #tk.Label(text=str(self.get_avg()), row=self.num+2, column=self.num+1)
        out = "you have an average grade of: " + str(avg) + "with combined weight of: " + str(weightt) + "%"

    def get_avg(self):
        avg = 0.00
        markt = 0
        weightt = 0
        rem = 0

        for i in range(self.num):
            if not self.weights[i].get() or not self.marks[i].get():
                break
            weight = int(self.weights[i].get())
            avg += float(self.marks[i].get()) * weight
            weightt += weight

        avg = avg / weightt
        avg = round(avg, 3)
        out1 = "you have an average grade of: " + str(avg)
        out2 = " with combined weight of: " + str(weightt) + "%"
        rem = 100 - weightt

        tk.Label(text=out1).grid(row=self.num+2, column=1)
        tk.Label(text=out2).grid(row=self.num+3, column=1)
