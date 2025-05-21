outFp = None
outStr = ""

fileName= input("파일 이름 입력: ")

outFp = open("C:\\pypy\\2025_python_practice_ykpark\\10주차\\fileTest\\%s.txt" %fileName, "w", encoding= 'UTF8')

while True:
    outStr = input("내용을 입력: ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close
print("--- 정상적으로 파일에 씀 ---")