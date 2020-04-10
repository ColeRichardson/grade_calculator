import tkinter as tk
from assignment import Assignment


class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UTM Grade Calculator")
        self.root.geometry("1000x700")
        self.root.configure(background='black')
        self.assignments = []
        self.num = 5
        self.avg_button = tk.Button(text="calculate average")
        self.add_button = tk.Button(text="add Assignment")
        self.delete_button = tk.Button(text="delete Assignment")
        for i in range(self.num):
            temp = Assignment(self.root)
            self.assignments.append(temp)
        self.setup_window()

    def setup_window(self):
        while len(self.assignments) < self.num:
            temp = Assignment(self.root)
            self.assignments.append(temp)

        for i in range(self.num):
            tk.Label(self.root, text='Assessment Name', background='white', padx=10, pady=10).grid(row=i)

        k = 0
        for ass in self.assignments:
            ass.name = tk.Entry(self.root, bg='orange')
            ass.name.grid(row=k, column=1)
            k+=1

        for i in range(self.num):
            tk.Label(self.root, text='Weight %', background='white', padx=10, pady=10).grid(row=i, column=2)

        k = 0
        for ass in self.assignments:
            ass.weight = tk.Entry(self.root, bg='orange')
            ass.weight.grid(row=k, column=3)
            k+=1
            
        for i in range(self.num):
            tk.Label(self.root, text='Grade %', background='white', padx=10, pady=10).grid(row=i, column=4)

        k = 0
        for ass in self.assignments:
            ass.mark = tk.Entry(self.root, bg='orange', justify='center')
            ass.mark.grid(row=k, column=5)
            k+=1

        #calculate the average button
        self.avg_button.destroy()
        self.avg_button = tk.Button(text="calculate average", command=self.get_avg)
        self.avg_button.grid(row=self.num+1, column=1)

        #add a new assignment box
        self.add_button.destroy()
        self.add_button = tk.Button(text="add Assignment", command=self.addField)
        self.add_button.grid(row=self.num+1, column=2)

        #delete an assignment box
        self.delete_button.destroy()
        self.delete_button = tk.Button(text="Delete Assignment", command=self.delField)
        self.delete_button.grid(row=self.num+1, column=3)

        self.root.mainloop()

    def addField(self):
        self.num += 1
        self.setup_window()

    def delField(self):
        self.num -= 1
        temp = self.assignments.pop()
        temp.name.destroy()
        temp.weight.destroy()
        temp.mark.destroy()
        self.setup_window()

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
