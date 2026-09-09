from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ", amount)
# this function is telling us to pass in an argument, but we won't tell you how or what kind
# of data it will be.
# (이 함수는 인자를 전달하라고 알려주지만, 어떤 방식이나 어떤 종류의 데이터가 될지는 알려주지 않습니다.)
    @abstractmethod
    def payment(self, amount):
        pass

class DebitCardPayment(car):
# here we've defined how to implement the payment function from its parent paySlip class.
# (여기서 우리는 부모 클래스의 payment 함수를 어떻게 구현할지 정의했습니다.)
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("$400")
obj.payment("$400")