class Car:
    color = ""
    speed = 0


    def __init__(self, value1, value2): #객체 생성시, 자동으로 실행이됨, 매서드 호출 안해도
        self.color = value1
        self.speed = value2
    
    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1= Car("빨강", 30)
myCar2= Car("파랑", 60)

print("자동차1의 색상은 %s이며, 현재 속도는 %dkm/h 입니다." %(myCar1.color, myCar1.speed))

print("자동차2의 색상은 %s이며, 현재 속도는 %dkm/h 입니다." %(myCar2.color, myCar2.speed))