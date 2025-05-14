from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc():
    if chk.get() == 0: #get은 현재 값 가져오기 함수
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

chk = IntVar() #위젯의 상태 저장하게 해주는 함수
cb1 = Checkbutton(window, text= "클릭하세요", variable= chk, command= myFunc)
cb1.pack()

window.mainloop()