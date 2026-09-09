# 1. 부모 클래스 생성
class Animal:
    def __init__(self, name):
        self.name = name  # 동물의 이름 속성
        
    # 부모 클래스의 기본 메서드 (자식 클래스들이 이 메서드를 덮어쓸 예정입니다)
    def make_sound(self):
        print(f"{self.name} makes a generic animal sound.")


# 2. 첫 번째 자식 클래스: Dog (Animal 상속)
class Dog(Animal):
    def __init__(self, name, breed, is_good_boy):
        # super()를 통해 부모 클래스의 name 속성을 가져옵니다.
        super().__init__(name)
        
        # Dog 클래스만의 고유한 속성 2가지
        self.breed = breed              # 고유 속성 1: 견종
        self.is_good_boy = is_good_boy  # 고유 속성 2: 착한 강아지인지 여부 (True/False)
        
    # 다형성(Polymorphism) 활용: 부모의 make_sound 메서드를 덮어씁니다!
    def make_sound(self):
        print(f"{self.name}, the {self.breed}, barks: Woof! Woof!")


# 3. 두 번째 자식 클래스: Cat (Animal 상속)
class Cat(Animal):
    def __init__(self, name, color, indoor_only):
        # super()를 통해 부모 클래스의 name 속성을 가져옵니다.
        super().__init__(name)
        
        # Cat 클래스만의 고유한 속성 2가지
        self.color = color              # 고유 속성 1: 털 색깔
        self.indoor_only = indoor_only  # 고유 속성 2: 실내묘 여부 (True/False)
        
    # 다형성(Polymorphism) 활용: 부모의 make_sound 메서드를 다르게 덮어씁니다!
    def make_sound(self):
        print(f"{self.name}, the {self.color} cat, meows: Meow! Purr...")


# --- 아래는 다형성이 어떻게 작동하는지 확인하기 위한 테스트 출력입니다 ---

# 객체 생성
generic_animal = Animal("Creature")
my_dog = Dog("Buddy", "Golden Retriever", True)
my_cat = Cat("Luna", "Black", True)

# 동일한 메서드 이름인 make_sound()를 호출하지만, 
# 다형성 덕분에 각 객체의 종류에 따라 완전히 다른 결과가 출력됩니다!
generic_animal.make_sound()  # 부모 클래스의 기본 소리 출력
my_dog.make_sound()          # 강아지는 짖는 소리 출력
my_cat.make_sound()          # 고양이는 야옹 소리 출력