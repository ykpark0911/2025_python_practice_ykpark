class Car : #공유
    color = "" #인스턴스 변수
    speed = 0 #인스턴스 변수
    count = 0 #클래스 변수

    def __init__(self):
        self.speed = 0
        Car.count += 1 #클레스 변수로써 쓰겠다

myCar1 = myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30
print("자동차 1의 현재 속도는 %dkm/h, 생산된 자동차는 총 %d대 입니다." %(myCar1.speed, Car.count))

myCar2 = Car()
myCar1.speed = 60
print("자동차 2의 현재 속도는 %dkm/h, 생산된 자동차는 총 %d대 입니다." %(myCar2.speed, Car.count))