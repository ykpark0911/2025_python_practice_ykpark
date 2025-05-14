from tkinter import *

window = Tk()
window.title("윈도창 연습")
window.geometry("400x100")
window.resizable(width= FALSE, height= FALSE)

label1 = Label(window, text = "COOKBOOK~~~Python을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg= "blue") #fg는 foreground(글자 색)
label3 = Label(window, text = "공부중입니다.", bg ="magenta", width= 20, height= 5, anchor= SE) #bg는 background(배경 색), anchor는 위젯이 어느 위치에 자리 잡을지, SE는 South-East

label1.pack()
label2.pack()
label3.pack()

window.mainloop()