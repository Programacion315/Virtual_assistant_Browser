from random import randint
import time
from tkinter import *

root = Tk()
root.overrideredirect(True) #Le quita el titulo, poner al final
root.wm_attributes('-transparentcolor', '#F0F0F0')

def move_me(x,y):
    x, y = str(x), str(y)
    loc = "300x265+" + x + '+' + y
    root.geometry(loc)
    x = int(x) + 2
    y = int(y) + 2

    if int(x) > 500:
        x = x - 2
        y = y - 2
    
    if int(x) % randint(1,1000) == 0:
        hack()
    root.after(10, move_me, x, y)
    
frameCnt = 60
frames = [PhotoImage(file='bowser.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(10, update, ind)
label = Label(root)
label.pack()

def hack():
        win = Toplevel(root)
        win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 60)))
        win.overrideredirect(1)
        Label(win, text="INFECTADO ", fg="red").place(relx=.3, rely=.3)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.05)

update(2)
move_me(2,2)

root.mainloop()