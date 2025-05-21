from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    if event.keycode == 37:
        key = "왼쪽"
    elif event.keycode == 38:
        key = "위쪽"
    elif event.keycode == 39:
        key = "오른쪽"
    elif event.keycode == 40:
        key = "아래쪽"
    messagebox.showinfo("키보드 이벤트", "눌린키 : Shift +" + key + " 화살표") #chr는 유니코드를 문자로 변환하는 함수

window = Tk()

window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Down>", keyEvent)
window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Right>", keyEvent)

window.mainloop()