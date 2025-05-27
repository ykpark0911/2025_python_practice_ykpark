from tkinter import *

window = Tk()

mainMenu = Menu(window) #메뉴바 만들겠다는 뜻
window.config(menu= mainMenu) #메뉴바를 윈도우창에 붙임

fileMenu = Menu(mainMenu) #'파일'이라는 하위 메뉴 묶음 만들기
mainMenu.add_cascade(label= "파일", menu= fileMenu) #메뉴바에 '파일'이라는 상위 메뉴 추가

fileMenu.add_command(label= "열기") #'파일' 안에 항목 추가
fileMenu.add_separator() # 구분선
fileMenu.add_command(label= "종료") #'파일' 안에 항목 추가

window.mainloop()