from tkinter import *

window = Tk()
buttoon1= Button(window, text="파이썬 종료", fg = "red", command = quit) #command는 버튼에서 클릭했을 때 호출할 함수를 지정, quit는 종료 함수

buttoon1.pack()
window.mainloop()