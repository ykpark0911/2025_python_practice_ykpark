class Car:
    name = ""
    speed = 0


    def __init__(self, name, speed): #생성자를 통해서 클래스의 필드를 조작할 수 있음
        self.name = name
        self.speed = speed
    
    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed

car1, car2 = None, None


Car1= Car("아우디", 0)
Car2= Car("벤츠", 30)

print("%s의 현재 속도는 %dkm/h 입니다." %(Car1.getName(), Car1.getSpeed()))
print("%s의 현재 속도는 %dkm/h 입니다." %(Car2.getName(), Car2.getSpeed())) 

print("%s의 현재 속도는 %dkm/h 입니다." %(Car1.name, Car1.speed))
print("%s의 현재 속도는 %dkm/h 입니다." %(Car2.name, Car2.speed))