from tkinter import *

window = Tk()

mainMenu = Menu(window) #메뉴바 만들겠다는 뜻
window.config(menu= mainMenu) #메뉴바를 윈도우창에 붙임

fileMenu = Menu(mainMenu) #mainMenu에 종속된 '파일'이라는 하위 메뉴 묶음 만들기
mainMenu.add_cascade(label= "파일", menu= fileMenu) #메뉴바(mainMenu)에 "파일"이라는 상위 항목을 추가하고
                                                    #→ 누르면 fileMenu에 있는 하위 항목이 드롭다운으로 보이게 됨

fileMenu.add_command(label= "열기") #'파일' 안에 기본 메뉴 항목 추가
fileMenu.add_separator() # 구분선
fileMenu.add_command(label= "종료") #'파일' 안에 기본 메뉴 항목 추가

window.mainloop()