from tkinter import *
from tkinter.filedialog import askopenfilename

def get_file():
    b_get_file(command = askopenfilename())

root = Tk()
root.geometry('200x120')

w = Label(root, text = 'Test').pack()
b_get_file = Button(root, text = "Open File", width = 40, command = get_file).pack()
b_generate = Button(root, text = 'Generate raport', width = 40).pack()
b_stop = Button(root, text='Stop', width=40, command=root.destroy).pack()
root.mainloop()