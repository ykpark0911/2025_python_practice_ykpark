from tkinter import *
from random import shuffle

btnList = [None] * 9
fnameList = ["cup-6614_128.gif", "bee-11531_128.gif", "dog-7011_128.gif", "listen-to-17266_128.gif",
             "pizza-13601_128.gif", "sun-15710_128.gif", "sun-18283_128.gif", "tractor-1972_128.gif", "ramadan-3976_128.gif"]

shuffle(fnameList)

photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

window = Tk()
window.geometry("384x384")

for i in range(0, 9) :
    photoList[i] = PhotoImage(file = "C:\\pypy\\2025_python_practice_ykpark\\9주차\\" + fnameList[i])
    btnList[i] = Button(window, image = photoList[i])

for i in range(0, 3) :
    for k in range(0, 3) :
        btnList[num].place(x = xPos, y = yPos)
        num += 1
        xPos += 128
    xPos = 0
    yPos += 128

window.mainloop()
