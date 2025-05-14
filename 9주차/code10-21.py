from tkinter import *
from tkinter.filedialog import *

window = Tk()
window.geometry("400x100")

label1 = Label(window, text= "입력된 값")
label1.pack()

saveFp = asksaveasfile(parent= window, mode= "w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg"), ("모든 파일", "*.*"))) #모듈을 통해 함수 사용
# mode=“w”는 쓰기 모드
# defaultextension=“.jpg”는 특별히 확장명을 지정하지 않으면 확장명을 jpg로 붙인다는 의미이 

label1.configure(text= saveFp)
saveFp.close