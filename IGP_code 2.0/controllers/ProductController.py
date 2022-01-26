from models.product import *

class ProductController:

    product_list = []

    def ProductGenerator(self, product_id, product_name, product_description, price_netto, price_brutto, category):
        individual_product = Product(product_id, product_name, product_description, price_netto, price_brutto, category)
        self.product_list.append(individual_product)

    def Print_Products(self):
        for individual_products in self.product_list:
            individual_products.ViewProducts()

    def addProducts(self, product_id, product_name, product_description, price_netto, price_brutto, category):
        added_product = Product(product_id, product_name, product_description, price_netto, price_brutto, category)
        self.product_list.append(added_product)

    def LoopProducts(self):
        for simple_pro in products:
            pc.ProductGenerator(simple_pro[0], simple_pro[1], simple_pro[2], simple_pro[3], simple_pro[4], simple_pro[5])

pc = ProductController()
pc.LoopProducts()





