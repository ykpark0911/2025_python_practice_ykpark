inFp, outFp = None, None
inStr, outStr = "", ""
i = 0
secu = 0

secyYN= input("1. 암호화 2. 암호해석 선택 :")
inFname= input("입력할 파일명을 입력하세요: ")
outFame = input("출력할 파일명을 입력하세요: ")

if secyYN == "1" :
    secu = 100
elif secyYN == "2" :
    secu = -100

inFp = open(inFname, "r", encoding= 'utf-8')
outFp = open(outFame, "w", encoding= 'utf-8')


while True:
    inStr = inFp.readline()
    if not inStr :
        break
    outStr = ""
    for i in range(0, len(inStr)) :
        ch = inStr[i]
        chNum = ord(ch)
        chNum += secu
        ch2 = chr(chNum)
        outStr = outStr + ch2


    outFp.writelines(outStr)


outFp.close()
inFp.close()
print("파일 정상적으로 복사 되었음")