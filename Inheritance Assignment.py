# 1. 부모 클래스 생성: 모든 전자기기의 공통 속성을 정의합니다.
class Device:
    def __init__(self, brand, model):
        self.brand = brand      # 제조사 속성
        self.model = model      # 모델명 속성

# 2. 첫 번째 자식 클래스: Smartphone (Device 클래스를 상속받음)
class Smartphone(Device):
    def __init__(self, brand, model, screen_size, battery_capacity):
        # super()를 사용하여 부모 클래스의 brand와 model 속성을 그대로 물려받습니다.
        super().__init__(brand, model)
        
        # Smartphone 클래스만의 고유한 속성 2가지를 추가합니다.
        self.screen_size = screen_size            # 고유 속성 1: 화면 크기
        self.battery_capacity = battery_capacity  # 고유 속성 2: 배터리 용량

# 3. 두 번째 자식 클래스: Laptop (Device 클래스를 상속받음)
class Laptop(Device):
    def __init__(self, brand, model, ram_size, has_touchscreen):
        # super()를 사용하여 부모 클래스의 brand와 model 속성을 그대로 물려받습니다.
        super().__init__(brand, model)
        
        # Laptop 클래스만의 고유한 속성 2가지를 추가합니다.
        self.ram_size = ram_size                  # 고유 속성 1: 램(RAM) 용량
        self.has_touchscreen = has_touchscreen    # 고유 속성 2: 터치스크린 지원 여부

# --- 아래는 코드가 잘 작동하는지 확인하기 위한 테스트 출력입니다 ---
# Smartphone 객체 생성 및 출력
my_phone = Smartphone("Apple", "iPhone 15", "6.1 inches", "3349mAh")
print(f"내 휴대폰: {my_phone.brand} {my_phone.model}, 배터리: {my_phone.battery_capacity}")

# Laptop 객체 생성 및 출력
my_laptop = Laptop("Samsung", "Galaxy Book", "16GB", True)
print(f"내 노트북: {my_laptop.brand} {my_laptop.model}, 램: {my_laptop.ram_size}")