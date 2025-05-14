#파일 존재 유무 확인하기
import os


inFp = None
fName, inLinst, inStr = "", [], ""


fName = input("파일 명을 입력하세요")

if os.path.exists(fName):
    inFp = open(fName, "r")
    inLinst = inFp.readlines()
    for inStr in inLinst:
        print(inStr, end = "")
    inFp.close()
else:
    print("%s 파일이 없습니다" % fName)