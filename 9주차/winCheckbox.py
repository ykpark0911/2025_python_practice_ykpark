from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc():
    if chk.get() == 0: #get은 IntVar의 실제 값을 뽑아내는 함수
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 켜졌어요.")

chk = IntVar() #위젯의 상태 저장하게 해주는 함수
cb1 = Checkbutton(window, text= "클릭하세요", variable= chk, command= myFunc) 
# variable = chk는 Checkbutton에 chk라는 데이터 박스를 연결한다 "variable = chk"는 곧 "chk = variable"처럼 동작... 양방향 데이터 바인딩
cb1.pack()

window.mainloop()