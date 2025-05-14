from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴 선택", "열기 메뉴를 선택함")

def func_exit():
    window.quit() #mainloop를 빠져나감
    window.destroy() #창 자체를 없애고 완전히 종료함


window = Tk()

mainMenu = Menu(window)
window.config(menu= mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label= "파일", menu= fileMenu)

fileMenu.add_command(label= "열기", command= func_open)
fileMenu.add_separator()
fileMenu.add_command(label= "종료", command= func_exit)

window.mainloop()