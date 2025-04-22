for i  in range(2, 10):
    print("#  {}단  # ".format(i), end="")

for num in range(1,10):
    print()
    for dan in range(2,10):
        print(f"{dan}X  {num}= {dan*num:>2} ", end = "")