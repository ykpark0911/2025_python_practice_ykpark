inFp, outFp = None, None

inFp = open("C:\\Windows\\win.ini", "r")
outFp = open("C:\\Temp\\data3.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("파일 정상적으로")