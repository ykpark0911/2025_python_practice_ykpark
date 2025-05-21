class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value

        print("현재 속도(슈퍼 클래스) : %d" % self.speed)

class Sedan(Car): #상속시킴
    def upSpeed(self, value): #오버 라이딩
        self.speed += value

        if self.speed > 150:
            self.speed = 150


            print("현재 속도(서브 클래스) : %d" % self.speed)

class Truck(Car):#상속시킴
    pass

sedan1, truck1= None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 --> ", end = "")
truck1.upSpeed(200) #트럭 은스턴스의 메서드 호출시, 슈퍼클레스의 메서드가  호출됨 

print("승용차 --> ", end = "")
sedan1.upSpeed(200)