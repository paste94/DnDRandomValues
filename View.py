from tkinter import ttk
import tkinter

from Controller import calculate_coins


class MyGui:
    def __init__(self, master):
        self.master = master.title("Prov")

        master.minsize(width=400, height=300)
        tkinter.Label(master, text='Grado sfida battuto: ').grid(row=0, column=0, sticky='w')

        tkinter.Label(master, text='Monete: ').grid(row=2, column=0, sticky='nw')
        message = tkinter.StringVar()

        message.set('')

        tkinter.Label(master, textvariable=message).grid(row=2, column=1, columnspan=2, sticky='w')
        answer = tkinter.ttk.Combobox(master)
        answer['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

        def get_cr():
            message.set(calculate_coins(answer.get()))

        answer.grid(row=0, column=1)
        tkinter.Button(master, text="Calcola", command=get_cr).grid(row=0, column=2)


top = tkinter.Tk()
MyGui(top)
top.mainloop()
