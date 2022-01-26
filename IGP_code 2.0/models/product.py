from models.warehouse import Warehouse
from addons.functions import *

class Product:

    product_id = None
    product_name = None
    product_description = None
    price_netto = None
    price_brutto = None
    category = None

    def __init__(self, product_id, product_name, product_description, price_netto, price_brutto, category):

        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.price_netto = price_netto
        self.price_brutto = price_brutto
        self.stock = Warehouse().stock
        self.category = category

    def ViewProducts(self):

        print("------------")
        print("Product_ID:", self.product_id)
        print("Product_name:", self.product_name)
        print("Description:", self.product_description)
        print("Price Netto", self.price_netto)
        print("Price Brutto:", self.price_brutto)
        print("In stock:", self.stock)
        print("Category:", self.category)

products = [[id_one, name_one, "Größe: 20cm, Länge: 54cm, Breite: 54cm", pg.price_netto(one_price), one_price, pg.product_category(name_one)],
           [id_two, name_two, "Größe: 40cm, Länge: 32cm, Breite: 88cm", pg.price_netto(two_price), two_price, pg.product_category(name_two)],
           [id_three, name_three, "Größe: 320cm, Länge: 53cm, Breite: 38cm", pg.price_netto(three_price), three_price, pg.product_category(name_three)],
           [id_four, name_four, "Größe: 2032cm, Länge: 12cm, Breite: 24cm", pg.price_netto(four_price), four_price, pg.product_category(name_four)],
           [id_five, name_five, "Größe: 12cm, Länge: 3cm, Breite: 12cm", pg.price_netto(five_price), five_price, pg.product_category(name_five)],
           [id_six, name_six, "Größe: 22cm, Länge: 87cm, Breite: 232cm", pg.price_netto(six_price), six_price, pg.product_category(name_six)],
           [id_seven, name_seven, "Größe: 56cm, Länge: 12cm, Breite: 794cm", pg.price_netto(seven_price), seven_price, pg.product_category(name_seven)],
           [id_eight, name_eight, "Größe: 231cm, Länge: 76cm, Breite: 77cm", pg.price_netto(eight_price), eight_price, pg.product_category(name_eight)],
           [id_nine, name_nine, "Größe: 123cm, Länge: 09cm, Breite: 70cm", pg.price_netto(nine_price), nine_price, pg.product_category(name_nine)],
           [id_ten, name_ten, "Größe: 54cm, Länge: 675cm, Breite: 87cm", pg.price_netto(ten_price), ten_price, pg.product_category(name_ten)]]

