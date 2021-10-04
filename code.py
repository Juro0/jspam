from tkinter import *
import pyautogui as p
from pyautogui import hotkey
import time

#var
v = 1

#creazione finestra
f = Tk()

#personalizzazione
f.title("Jspam")
f.geometry("450x250")
f.configure(bg="#c0c0c0")

#funzioni
def spamma():
    v = int(write2.get())
    f.clipboard_clear()
    f.clipboard_append(write.get())
    time.sleep(5)
    for i in range(v):
        p.hotkey('ctrl','v')
        p.hotkey('enter')

#widget
testo1 = Label(f, text="JSPAM", background="#c0c0c0", font="Times 11 bold")
testo1.pack(side=TOP)
testo1.configure(foreground="black")

testo2 = Label(f, text="testo da spammare:", background="#c0c0c0")
testo2.pack(pady=5)

b = Button(f, text="spamma!", command=spamma)
b.pack(side=BOTTOM)
b.configure(cursor="hand2")

write = Entry(f)
write.pack(pady=3)
write.insert(0, "Scrivi qui...")

testo2 = Label(f, text="Quante volte vuoi spammare:", background="#c0c0c0")
testo2.pack(pady=3)

write2 = Entry(f)
write2.pack(pady=3)
write2.insert(0, "3")

testo3 = Label(f, text="Una volta cliccato spamma avrai 5 secondi per posizionare il tuo cursore nel punto in cui vuoi spammare", background="#c0c0c0", font="Times 6 italic")
testo3.pack(side=BOTTOM, pady=3)

#fine finestra
f.mainloop()
