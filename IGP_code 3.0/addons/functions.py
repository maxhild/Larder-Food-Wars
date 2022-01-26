import datetime, random
from addons.user_id_generator import users_id
from flask import render_template

normalizer = lambda input: input.lower()

def name_validation(name):

    while len(name) < 3 or name[0].isupper() is not True:
        return render_template("createAccount.html", result="Sorry")
    if len(name) < 3 or name[0].isupper() is True:
        return render_template("createAccount.html", result="True")

class Productgenerator():
    def Product_ID(self):
        product = users_id()
        return product

    def produktname(self):
        product_name_list = ["Apocalypse Now", "Früchte des Zorns", "Logitech Tastatur", "Honda Civic", "Kopfhörer Bose",
                             "Queen Mary", "Gtx 970", "Samsung 21", "Bier", "Nike Schuhe"]
        random.shuffle(product_name_list)
        shuffled_product_list = []
        name = 0
        for product_name in product_name_list:
            while name < 1:
                shuffled_product_list.append(product_name)
                name += 1
        return shuffled_product_list[0]

    def price_brutto(self):

        price_brutto = random.randint(0, 1000)
        return price_brutto

    def price_netto(self, price_brutto):
        return round(price_brutto - (price_brutto * 0.10))

    def product_category(self, produktname):
        if produktname == "Apocalypse Now" or produktname == "Früchte des Zorns":
            category = "Movies and Books"
            return category

        elif produktname == "Kopfhörer Bose" or produktname == "Logitech Tastatur" or produktname == "Gtx 970" or produktname == "Samsung 21":
            category = "Technic"
            return category

        else:
            category = "others"
            return category

pg = Productgenerator()


name_one, one_price, id_one = "Logitech Keyboard", pg.price_brutto(), pg.Product_ID()
name_two, two_price, id_two = "Samsung 21", pg.price_brutto(), pg.Product_ID()
name_three, three_price, id_three = "Früchte des Zorns", pg.price_brutto(), pg.Product_ID()
name_four, four_price, id_four = "Kopfhörer Bose", pg.price_brutto(), pg.Product_ID()
name_five, five_price, id_five = "Gtx 970", pg.price_brutto(), pg.Product_ID()
name_six, six_price, id_six = "Bier", pg.price_brutto(), pg.Product_ID()
name_seven, seven_price, id_seven = "Nike Schuhe", pg.price_brutto(), pg.Product_ID()
name_eight, eight_price, id_eight = "Apocalypse Now", pg.price_brutto(), pg.Product_ID()
name_nine, nine_price, id_nine = "Honda Civic", pg.price_brutto(), pg.Product_ID()
name_ten, ten_price, id_ten = "Queen Mary", pg.price_brutto(), pg.Product_ID()

def updated_data(change_attribut, value):
    if change_attribut == "firstname":
        firstname = value
        return firstname

    elif change_attribut == "lastname":
        lastname = value
        return lastname

    elif change_attribut == "birthday":
        birthday = value
        return birthday

def quit_function(input_command):
    if input_command == "quit":
        print("Terminates Program")
        return quit()
