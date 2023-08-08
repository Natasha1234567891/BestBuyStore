class Product:

    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True
        if name == "":
            raise ValueError("The name can't be empty")
        elif price < 0:
            raise ValueError("The price can't be negative")
        elif quantity < 0:
            raise ValueError("The quantity can't be negative")

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("The quantity can't be negative")
        elif quantity == 0:
            self.active = False
        self._quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self._name}, Price:{self._price}, Quantity: {self._quantity}"

    def buy(self, quantity):
        if self._quantity >= quantity:
            self._quantity -= quantity
            total_price = self._price * quantity
        else:
            raise ValueError("We don't have this amount of product in the store")
        return total_price


if __name__ == '__main__':
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())
    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())
