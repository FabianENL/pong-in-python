import tkinter as tk
import os

locatie = os.getcwd()

root= tk.Tk()

def onevone_multi():
    root.destroy()
    os.system('cd ' + str(locatie) + ' && python 1v1-multi-v2.py')
    exit()

def solo():
    root.destroy()
    os.system('cd ' + str(locatie) + ' && python solo.py')
    exit()

def with_ai():
    root.destroy()
    os.system('cd ' + str(locatie) + ' && python with-ai.py')
    exit()

    

canvas1 = tk.Canvas(root, width = 800, height = 600,  relief = 'raised')


label1 = tk.Label(root, text='Pong in python')
label1.config(font=('helvetica', 20))
canvas1.create_window(400, 25, window=label1)

button1 = tk.Button(text='2 player 1v1', command=onevone_multi, bg='blue', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(400, 200, window=button1)

button2 = tk.Button(text='solo pong', command=solo, bg='blue', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(400, 300, window=button2)

button3 = tk.Button(text='vs ai', command=with_ai, bg='blue', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(400, 400, window=button3)

canvas1.pack()
root.mainloop()
