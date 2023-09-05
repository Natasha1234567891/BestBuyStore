class Product:

    def __init__(self, name, price, quantity, promotion=None):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._promotion = promotion

        if self._quantity > 0:
            self.active = True
        else:
            self.active = False

        if name == "":
            raise ValueError("The name can't be empty")
        elif price < 0:
            raise ValueError("The price can't be negative")
        elif quantity < 0:
            raise ValueError("The quantity can't be negative")

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

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
        if self._promotion is None:
            return f"{self._name}, Price:{self._price}, Quantity: {self._quantity}"
        else:
            return f"{self._name}, Price:{self._price}, Quantity: {self._quantity}, Promotion:{self._promotion.get_name()}"

    def set_promotion(self, promotion):
        self._promotion = promotion

    def buy(self, quantity):
        if self._quantity < quantity:
            raise ValueError("We don't have this amount of product in the store")

        self._quantity -= quantity
        if self._promotion is None:
            total_price = self._price * quantity
        else:
            total_price = self._promotion.apply_promotion(self,quantity)
        return total_price


class Non_stocked_product(Product):
    def __init__(self, name, price, promotion=None):
        super().__init__(name, price, 0, promotion)

    def is_active(self):
        return True

    def buy(self, quantity):
        if self._promotion is None:
            total_price = self._price * quantity
        else:
            total_price = self._promotion.apply_promotion(self, quantity)
        return total_price


class Limited_product(Product):
    def __init__(self, name, price, quantity, maximum_quantity, promotion=None):
        super().__init__(name, price, quantity, promotion)
        self._maximum_quantity = maximum_quantity

    def get_maximum_quantity(self):
        return self._maximum_quantity

    def set_maximum_quantity(self, maximum_quantity):
        if maximum_quantity < 0:
            raise ValueError("The quantity can't be negative")
        self._maximum_quantity = maximum_quantity

    def show(self):
        return f"{self._name}, Price:{self._price}, Quantity: {self._quantity}, Maximum quantity: {self._maximum_quantity}"

    def buy(self, quantity):
        if self._quantity < quantity:
            raise ValueError("We don't have this amount of product in the store")
        if self._maximum_quantity < quantity:
            raise ValueError("We can't sell this amount of product")

        self._quantity -= quantity
        if self._promotion is None:
            total_price = self._price * quantity
        else:
            total_price = self._promotion.apply_promotion(self, quantity)
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
