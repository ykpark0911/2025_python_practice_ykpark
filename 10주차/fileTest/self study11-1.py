inFp = None
inStr = ""
num = 0

inFp = open("C:\\pypy\\2025_python_practice_ykpark\\10주차\\fileTest\\text.txt", "r", encoding= 'UTF8')

while True:
    num += 1
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" %(num, inStr), end = "")


inFp.close()