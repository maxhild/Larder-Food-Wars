from controllers.ProductController import ProductController
from models.product import Product

product = Product
pc = ProductController

class CartController:

    cart_list = []

    def find_product(self, product_id):
        for products in pc.product_list:
            if products.product_id == product_id:
                return products

    def add_product_cart(self, product, number_products):

        product = self.find_product(product)
        number_products = int(number_products)

        if product is None:

            print("The product-id does not exist!")

        elif product is not None and product.stock >= number_products:

            number = 0
            while number < number_products:

                self.cart_list.append(product)
                number += 1
        else:
            try:
                print("Sorry,the product is no longer available in this quantity!")
                print("There only:", product.stock, "available. You selected:", number_products, "products.")
            except:
                print("Sorry,the product is no longer available in this quantity!")

    def View_Cart(self):

        for counter, product in enumerate(self.cart_list):
            print("Product in Cart no.", counter + 1)
            product.stock = product.stock - 1
            product.ViewProducts()
        print("Total Products in Cart", counter + 1, "Still", product.stock, "available")

    def ViewTotalCost(self, product, number_products):

            product = self.find_product(product)

            product_total_price = int(product.price_netto) * int(number_products)

            return product_total_price

    #noch auf user zuschneiden
    def DeleteCart(self, cart_id):
        cart_list = self.cart_list.copy()
        for cart in cart_list:

            if cart.product_id == cart_id:

                self.cart_list.remove(cart)




