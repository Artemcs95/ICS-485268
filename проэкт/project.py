from tkinter import *
from data import *
from graphik import graph
from opentable import opentable
from to_json import convertToJSON
from to_json import convertInJSON

columns = len(nounlist)
columns2 = len(nounlist2)



def openTable():
    opentable()
    root = Tk()
    root.geometry('200x100')
    root.title('Таблиця.')
    lbl = Label(root)
    lbl.configure(font=(7), text="Таблиця в консолі.")
    lbl.place(x=0, y=0)
    root.mainloop()


def JSON():
    convertToJSON()
    root_2 = Tk()
    root_2.geometry('356x70')
    root_2.resizable(False, False)
    root.title('файл ')
    lbl = Label(root_2)
    lbl.configure(font=(8), text='Файл у форматі JSON зроблено.')
    lbl.place(x=4, y=2)
    root_2.mainloop()

def create_JSON():
    convertInJSON()
    root_3 = Tk()
    root_3.geometry('356x50')
    root_3.resizable(False, False)
    root_3.title('Повідомлення.')
    lbl = Label(root_3)
    lbl.configure(font = (10), text = 'Файл у форматі JSON зроблено.')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()


def selection(event):
    searchbtn.selection_range(0, END)


root = Tk()
root.title("Зміна рівня ринкових цін")
root.geometry("600x450")
root.configure(bg = '#FAEBD7')
btn1 = Button(root, text='Подивитися графік', bg='#4682B4', fg='pink', borderwidth=0, command=graph)
btn1.place(x=200, y=70, height=35, width=200)
btn2 = Button(root, text='Зробити JSON файл таблиці \n цін продуктів по місяцях', bg='#4682B4', fg='pink',
              borderwidth=0, command=JSON)
btn2.place(x=200, y=115, height=35, width=200)
btn3 = Button(root, text='Зробити JSON файл таблиці \nдовіднику товару', bg='#4682B4', fg='pink', borderwidth=0,
              command=create_JSON)
btn3.place(x=200, y=160, height=35, width=200)
btn4 = Button(root, text='Переглянути таблицю', bg='#4682B4', fg='pink', borderwidth=0,
              command=openTable)
btn4.place(x=200, y=205, height=35, width=200)

root.mainloop()