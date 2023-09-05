from product import Product, Limited_product, Non_stocked_product
from store import Store
from promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree


def start():
    print(
        """        Store Menu:
        -----------
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """)
    choice = input("Please choose a number: ")
    return choice


def main():
    # product_list = [Product("MacBook Air M2", price=1450, quantity=100),
    #                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    #                 Product("Google Pixel 7", price=500, quantity=250),
    #                 ]
    # store = Store(product_list)
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    Non_stocked_product("Windows License", price=125),
                    Limited_product("Shipping", price=10, quantity=250, maximum_quantity=1)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    store = Store(product_list)
    while True:
        choice = start()
        print()

        if choice == "1":
            for product in store.get_all_products():
                print(product.show())
        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store")
        elif choice == "3":

            while True:
                print("When you want to finish order, enter empty text.")
                product_number = input("Which product # do you want?")
                amount_of_product = input("What amount do you want?")
                if product_number == "" or amount_of_product == "":
                    break
                else:
                    product_number = int(product_number)
                    amount_of_product = int(amount_of_product)
                    if product_number <= len(product_list):
                        try:
                            product_list[product_number - 1].buy(amount_of_product)
                            print("Product added to list!")
                        except ValueError:
                            print("We don't have this amount of product in the store")
                    else:
                        print("Error adding product!")
        elif choice == "4":
            print("Bye!")
            break

        print()


if __name__ == '__main__':
    main()
