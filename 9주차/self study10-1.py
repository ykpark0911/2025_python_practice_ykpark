from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\pypy\\2025_python_practice_ykpark\\9주차\\스크린샷 2025-05-06 143329.png")
photo2 = PhotoImage(file = "C:\\pypy\\2025_python_practice_ykpark\\9주차\\스크린샷 2025-05-06 144017.png")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo1)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()