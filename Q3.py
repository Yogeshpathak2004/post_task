""" Create Abstract class Payment with: 
• Abstract method pay()
• Abstract method receipt()
Create 2 child classes: GPay and CreditCard — implement both methods.
Create objects and call all methods"""

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def receipt(self):
        pass


class GPay(Payment):
    def pay(self):
        print("Payment done through GPay")

    def receipt(self):
        print("GPay Receipt Generated")


class CreditCard(Payment):
    def pay(self):
        print("Payment done through Credit Card")

    def receipt(self):
        print("Credit Card Receipt Generated")


gpay = GPay()
gpay.pay()
gpay.receipt()

card = CreditCard()
card.pay()
card.receipt()