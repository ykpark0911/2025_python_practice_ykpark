from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text= "입력된 값")
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)", minvalue= 1, maxvalue= 6) #모듈을 통해 함수 사용
# askinteger(“제목”, “내용”, 옵션)

label1.configure(text= str(value))
window.mainloop()