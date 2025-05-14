#파일에서 읽어서 모니터에 출력하기
inFp = None
inStr = ""


inFp = open("C:\\pypy\\2025 python practice ykpark\\10주차\\fileTest\\text.txt", "r", encoding= 'UTF8')

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end = "")


inFp.close()