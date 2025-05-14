from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\user\\Downloads\\용 왼쪽.png")
photo2 = PhotoImage(file = "C:\\Users\\user\\Downloads\\용 왼쪽.png")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo1)

label1.pack(side=LEFT) #LEFT는 왼쪽에서 오른쪽으로, TOP(기본), RIGHT, BOTTOM 존재
label2.pack(side=LEFT)

window.mainloop()