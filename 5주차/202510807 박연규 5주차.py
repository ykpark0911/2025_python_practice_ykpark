for i in range(2, 10):
    print("#  {}단  # ".format(i), end = "")

for num in range(1, 10): #계수
    print()
    for dan in range(2, 10): #단
        print("{} {:>2} ".format(f"{dan}X  {num}=", f"{dan*num}"), end = "")