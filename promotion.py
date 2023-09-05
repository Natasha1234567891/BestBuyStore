class Promotion:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self._percent = percent

    def apply_promotion(self, product, quantity):
        price = product.get_price()
        final_price = (100 - self._percent) / 100 * quantity * price
        return final_price


class SecondHalfPrice(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        price = product.get_price()
        half_quantity = quantity // 2
        remainder_of_division = quantity % 2
        final_price = (1.5 * half_quantity + remainder_of_division) * price
        return final_price


class ThirdOneFree(Promotion):

    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        price = product.get_price()
        third_quantity = quantity // 3
        remainder_of_division = quantity % 3
        final_price = (2 * third_quantity + remainder_of_division) * price
        return final_price
