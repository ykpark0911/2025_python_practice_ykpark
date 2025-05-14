from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text= "입력된 값")
label1.pack()

 #모듈을 통해 함수 사용
filename = askopenfilename(parent= window, filetypes=(("GIF 파일", "*.gif"), ("모든 파일", "*.*")))# askopenfilename(filetypes(필터 옵션들))
#parent= window는 파일 선택 창이 이 window 위에서 뜨게 함

label1.configure(text= str(filename))
window.mainloop()