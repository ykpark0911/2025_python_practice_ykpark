from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린키 :" +chr(event.keycode)) #chr는 유니코드를 문자로 변환하는 함수

window = Tk()

window.bind("<Key>", keyEvent)

window.mainloop()