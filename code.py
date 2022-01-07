from tkinter import *
import pyautogui as p
from pyautogui import hotkey
import time

#var
v = 1

# windows
f = Tk()

# custom win
f.title("Jspam")
f.geometry("450x250")
f.configure(bg="#c0c0c0")

# def
def spamma():
    v = int(write2.get())
    f.clipboard_clear()
    f.clipboard_append(write.get())
    time.sleep(5)
    for i in range(v):
        p.hotkey('ctrl','v')
        p.hotkey('enter')

# widgets
testo1 = Label(f, text="JSPAM", background="#c0c0c0", font="Times 11 bold")
testo1.pack(side=TOP)
testo1.configure(foreground="black")

testo2 = Label(f, text="Text:", background="#c0c0c0")
testo2.pack(pady=5)

b = Button(f, text="spam!", command=spamma)
b.pack(side=BOTTOM)
b.configure(cursor="hand2")

write = Entry(f)
write.pack(pady=3)
write.insert(0, "Write here...")

testo2 = Label(f, text="How many time:", background="#c0c0c0")
testo2.pack(pady=3)

write2 = Entry(f)
write2.pack(pady=3)
write2.insert(0, "3")

testo3 = Label(f, text="Once you click spam you will have 5 seconds to place your cursor where you want to spam", background="#c0c0c0", font="Times 6 italic")
testo3.pack(side=BOTTOM, pady=3)

# mainloop
f.mainloop()
