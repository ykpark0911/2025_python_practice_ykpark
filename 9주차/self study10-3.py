from tkinter import *
from time import *

fnameList = ["cup-6614_128.gif", "bee-11531_128.gif", "dog-7011_128.gif", "listen-to-17266_128.gif",
             "pizza-13601_128.gif", "sun-15710_128.gif", "sun-18283_128.gif", "tractor-1972_128.gif", "ramadan-3976_128.gif"]

photoList = [None] * 9
num = 0


def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = PhotoImage(file = "C:\\pypy\\2025_python_practice_ykpark\\9주차\\" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image= photo

def clickPtev():
    global num
    num += -1
    if num < 0:
        num = 8
    photo = PhotoImage(file = "C:\\pypy\\2025_python_practice_ykpark\\9주차\\" + fnameList[num])
    pLabel.configure(image = photo)
    pLabel.image= photo

window = Tk()
window.geometry("700x700")
window.title("사진 앨범 보기")


btnPrv = Button(window, text= "<< 이전", command= clickPtev)
btnNext = Button(window, text= "다음 >>", command= clickNext)

photo = PhotoImage(file= "C:\\pypy\\2025_python_practice_ykpark\\9주차\\" + fnameList[0])
pLabel = Label(window, image= photo)
title = Label(window, text= fnameList[num])

btnPrv.place(x = 200, y = 10)
btnNext.place(x= 450, y = 10)
title.place(x= 300, y= 10)
pLabel.place(x= 15, y= 50)


window.mainloop()
