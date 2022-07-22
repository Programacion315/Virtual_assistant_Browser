from random import randint
import time
from tkinter import *
import ctypes
from urllib import response
import requests

root = Tk()
#root.overrideredirect(True) #Le quita el titulo, poner al final
root.wm_attributes('-transparentcolor', '#F0F0F0')


def getJoke():
    joke = requests.get(f"https://icanhazdadjoke.com/", headers= {"Accept":"application/json"})
    joke = joke.json() 
    print(joke['joke'])
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Message")
    loc = "900x200+1+1"
    ventana_secundaria.geometry(loc)

    
    Label(ventana_secundaria, text=joke['joke'],
             font=("Agency FB", 14)).place(x=50, y=50) 
    


def position():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    restaAncho = int(ancho * 0.20)
    restaAlto = int(alto * 0.40)
    x, y = str(ancho - restaAncho), str(alto - restaAlto)
    loc = "300x265+" + x + '+' + y
    root.geometry(loc)
   
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

getJoke()
position()
update(2)

root.mainloop()