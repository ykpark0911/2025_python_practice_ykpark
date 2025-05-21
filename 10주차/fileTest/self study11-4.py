inFp, outFp = None, None

source = input("소스 파일명 입력하세요: ") #C:\pypy\2025_python_practice_ykpark\10주차\fileTest\text.txt
tartget= input("타깃 파일명 입력하세요: ") #C:\\pypy\\2025_python_practice_ykpark\\10주차\\fileTest\\data3.txt

inFp = open(source, "r", encoding= 'UTF8')
outFp = open(tartget, "w", encoding= 'UTF8')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---%s파일 %s파일로 복사되었음---" %(source, tartget))