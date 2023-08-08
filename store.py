class Store:

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        final_quantity = 0
        for product in self.product_list:
            final_quantity += product.get_quantity()
        return final_quantity

    def get_all_products(self):
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for each_tuple in shopping_list:
            try:
                total_price += each_tuple[0].buy(each_tuple[1])
            except ValueError:
                print("We don't have this amount of product in the store")
        return total_price

