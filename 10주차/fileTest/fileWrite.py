outFp = None
outStr = ""

outFp = open("C:\\pypy\\2025 python practice ykpark\\10주차\\fileTest\\data2.txt", "w")

while True:
    outStr = input("내용을 입력")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close
print("정상저그로 파일에 씀")