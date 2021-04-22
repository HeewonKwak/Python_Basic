class Unit:
    def __init__(self):
        print("유닛 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
        #super은 다중 상속에는 사용 못함 맨 처음만 상속됨
        # Unit.__init__(self)
        # Flyable.__init__(self)

dropship = FlyableUnit()

