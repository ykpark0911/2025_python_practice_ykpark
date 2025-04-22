#각 단의 제목 출력
for i in range(2, 10):
    print(f"#  {i}단  # ", end = "") #end = "" 는 줄바꿈 하지 않겠다는 것을 의미

#각 (세로)줄을 출력
for num in range(1, 10): #num: 곱해지는 수
    print()

    for dan in range(2, 10): #dan: 단
        print(f"{dan}X  {num}= {dan*num:2} ", end = "") # "{단}X  {곱해지는 수}= {결과} " 형식으로 출력 ({결과}는 2칸 확보 후 오른쪽 정렬)