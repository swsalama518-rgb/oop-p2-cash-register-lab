#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.previous_transactions = []
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, value):
        if 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
    def add_item(self, item, price, quantity = 1):
        self.total += price * quantity
        self.previous_transactions.append((item, price, quantity))
        for _ in range(quantity):
            self.items.append(item)
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total * (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
    def void_last_transaction(self):
        last_transaction = self.previous_transactions[-1]
        item, price, quantity = last_transaction
        self.previous_transactions.pop()
        self.total -= price * quantity
        self.items.pop()
register = CashRegister(20)
register.add_item("eggs", 1.99, 2)
register.add_item("tomatoes", 1.76, 3)
register.add_item("apples", 0.99, 1)
register.apply_discount()
register.void_last_transaction()
print(register.items)
print(register.total)
print(register.previous_transactions)