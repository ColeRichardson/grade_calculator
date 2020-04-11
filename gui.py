import tkinter as tk
from assignment import Assignment

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("UTM Grade Calculator")
        self.root.geometry("1000x700")
        self.root.configure(background='black')
        self.assignments = []
        self.num = 5 # minimum number of asssignments
        self.limit = 10 # maximum number of assignments allowed
        self.avg_button = tk.Button(text="calculate average")
        self.add_button = tk.Button(text="add Assignment")
        self.delete_button = tk.Button(text="delete Assignment")
        self.setup_window()

    def setup_window(self):
        #while (len(self.assignments) < self.num) and (self.num < self.limit):
            #temp = Assignment(self.root)
            #self.assignments.append(temp)

        for i in range(len(self.assignments)):
            if len(self.assignments) > self.limit:
                break
            # name
            self.assignments[i].name_label = tk.Label(self.root, text='Assessment Name', background='white', padx=10, pady=10)
            self.assignments[i].name_label.grid(row=i, column=0)
            self.assignments[i].name = tk.Entry(self.root, bg='orange')
            self.assignments[i].name.grid(row=i, column=1)
            # weight
            self.assignments[i].weight_label = tk.Label(self.root, text='Weight %', background='white', padx=10, pady=10)
            self.assignments[i].name_label.grid(row=i, column=2)
            self.assignments[i].weight = tk.Entry(self.root, bg='orange')
            self.assignments[i].weight.grid(row=i, column=3)
            # mark
            self.assignments[i].mark_label = tk.Label(self.root, text='Grade %', background='white', padx=10, pady=10)
            self.assignments[i].name_label.grid(row=i, column=4)
            self.assignments[i].mark = tk.Entry(self.root, bg='orange', justify='center')
            self.assignments[i].mark.grid(row=i, column=5)

        #calculate the average button
        self.avg_button.destroy()
        self.avg_button = tk.Button(text="calculate average", command=self.get_avg)
        self.avg_button.grid(row=len(self.assignments)+1, column=1)

        #add a new assignment box
        self.add_button.destroy()
        self.add_button = tk.Button(text="add Assignment", command=self.addField)
        self.add_button.grid(row=len(self.assignments)+1, column=2)

        #delete an assignment box
        self.delete_button.destroy()
        self.delete_button = tk.Button(text="Delete Assignment", command=self.delField)
        self.delete_button.grid(row=len(self.assignments)+1, column=3)

        self.root.mainloop()

    def addField(self):
        if len(self.assignments) < self.limit:
            temp = Assignment(self.root)
            self.assignments.append(temp)
            self.setup_window()

    def delField(self):
        if 0 < len(self.assignments) < self.limit:
            temp = self.assignments.pop()
            temp.name_label.destroy()
            temp.name.destroy()
            temp.weight_label.destroy()
            temp.weight.destroy()
            temp.mark_label.destroy()
            temp.mark.destroy()
            self.setup_window()

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

        tk.Label(text=out1).grid(row=11, column=1)
        tk.Label(text=out2).grid(row=11, column=1)
