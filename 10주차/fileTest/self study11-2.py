inFp = None
inLinst, inStr = [], ""
num = 0


inFp = open("C:\\pypy\\2025_python_practice_ykpark\\10주차\\fileTest\\text.txt", "r", encoding= 'UTF8')

inList= inFp.readlines()

for inStr in inList:
    num += 1
    print("%d: %s" %(num, inStr), end = "")

inFp.close()