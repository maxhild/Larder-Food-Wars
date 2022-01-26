from flask import Flask, render_template, request, session
from controllers.AccountController import AccountController
from controllers.PaymentCustomerDataController import PaymentCustomerDataController
from controllers.CartController import CartController
from controllers.Warehouse_Controller import WarehouseController
from controllers.CustomerReviewController import *
from addons.functions import *
from models.warehouse import Warehouse
from flask_login import logout_user

ac = AccountController()
pc = ProductController()
cc = CartController()
crc = CustomerReviewController()
pcdc = PaymentCustomerDataController()
wc = WarehouseController()

app = Flask(__name__, template_folder="../app/templates", static_folder="../app/static")

app.secret_key = "pwemdiopwed32sad3"

@app.route("/")
def loginpage():
    return render_template("loginpage.html")

@app.route("/createAccount")
def createaccount():
    return render_template("createAccount.html")

@app.route("/startpage_per_login", methods=["POST"])
def admin_startpage():
    login_username = request.form.get("login_username")
    login_password = request.form.get("login_password")
    login_func = ac.login(username=login_username, password=login_password)
    session["login_username"] = login_username
    session["login_password"] = login_password

    if login_func is None or login_func is False:

        return render_template("loginpage.html", result_login="Sorry the combination of username and password is incorrect!")

    elif login_func == 'admin':
        return render_template("admin/startpage_admin.html")

    elif login_func == 'customer':
        return render_template("startpage.html")

@app.route("/validation", methods=["POST"])
def validation():
    user_ID = users_id()
    username = request.form.get("username")
    session["username"] = username
    firstname = request.form.get("firstname")

    while len(firstname) < 3 or firstname[0].isupper() is not True:
        return render_template("createAccount.html", result_firstname="Your firstname must have at least 3 characters and the first letter capitalized!", style="alert alert-danger")

    session["firstname"] = firstname

    lastname = request.form.get("lastname")

    while len(lastname) < 3 or lastname[0].isupper() is not True:
        return render_template("createAccount.html", result_lastname="Your lastname must have at least 3 characters and the first letter capitalized!",style="alert alert-danger")
    session["lastname"] = lastname

    birthday = request.form.get("birthday")

    if len(birthday) >= 10:
        year, month, day = birthday.split('-')
        try:
            datetime.date(int(year), int(month), int(day))
        except ValueError:
            return render_template("createAccount.html", result_birthday="The date has no correct format!", style="alert alert-danger")

    elif len(birthday) < 10:
        return render_template("createAccount.html", result_birthday="The date is incomplete!", style="alert alert-danger")
    session["birthday"] = birthday

    password = request.form.get("password")
    repeat_password = request.form.get("password_repeat")

    if password != repeat_password:
        return render_template("createAccount.html", result_repeat_password="Sorry different password!", style="alert alert-danger")

    digit, lower, upper = False, False, False

    while password is not True:
        if len(password) >= 8 and len(password) <= 15:
            for p in password:
                if p.isdigit():
                    digit = True
                if p.islower():
                    lower = True
                if p.isupper():
                    upper = True

            if digit and lower and upper == True:

                session["password"] = password
                ac.create_customer_account(firstname=firstname, lastname=lastname, birthday=birthday, user_ID=user_ID,
                                           username=username, password=password)

                return render_template("quiz.html")
            else:
                return render_template("createAccount.html", result_password="Password has to contain at least a digit, uppercase and lowercase letter!",
                                       style="alert alert-danger")
        else:
            return render_template("createAccount.html", result_password="Password has to contain at least a digit, uppercase and lowercase letter!", style="alert alert-danger")

@app.route("/showproducts", methods=["POST"])
def show_products():
    productlist = pc.product_list
    stock = Warehouse().stock
    return render_template("admin/products_admin.html", productlist=productlist, stock=stock)

@app.route("/link_add_products", methods=["POST"])
def link_add_products():
    return render_template("admin/add_products_admin.html")

@app.route("/add_products", methods=["POST"])
def add_products():
    product_id = request.form.get("product_id")
    product_name = request.form.get("product_name")
    product_description = request.form.get("product_description")
    price_netto = request.form.get("price_netto")
    price_brutto = request.form.get("price_brutto")
    product_category = request.form.get("product_category")
    pc.ProductGenerator(product_id, product_name, product_description, price_netto, price_brutto, product_category)
    productlist = pc.product_list
    stock = Warehouse().stock
    return render_template("admin/products_admin.html", productlist=productlist, stock=stock)

@app.route("/show_products_customer", methods=["POST"])
def show_products_customer():
    productlist = pc.product_list
    stock = Warehouse().stock
    return render_template("products_customer.html", productlist=productlist, stock=stock)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    add_to_cart = request.form.get("product_id")
    number_products = request.form.get("quantity")
    product = cc.find_product(add_to_cart)
    number_products = int(number_products)
    productlist = pc.product_list
    if product is None:
        return render_template("products_customer.html", result_stock="Sorry product does not exist!", style="alert alert-danger")

    elif product.stock <= number_products:
        return render_template("products_customer.html", available="available. You choose", number_products=number_products,
                     product_stock=product.stock, style="alert alert-danger", productlist=productlist)

    cc.add_product_cart(add_to_cart, number_products)
    session["product_id"] = add_to_cart
    session["quantity"] = number_products
    cartlist = cc.cart_list
    total_cost = cc.ViewTotalCost(add_to_cart, number_products)
    session["total_cost"] = total_cost
    return render_template("cart_customer.html", cartlist=cartlist, total_cost=total_cost)

@app.route("/link_checkout", methods=["POST"])
def link_checkout():
    return render_template("checkout.html")

@app.route("/checkout", methods=["POST"])
def checkout():
    street = request.form.get("street")
    session["street"] = street
    add_to_cart = session["product_id"]
    housenumber = request.form.get("housenumber")
    zip_code = request.form.get("zip_code")
    credit_card_name = request.form.get("credit_card_name")
    credit_card_num = request.form.get("credit_card_num")
    credit_card_month = request.form.get("credit_card_month")
    credit_card_month = int(credit_card_month)
    credit_card_year = request.form.get("credit_card_year")
    cvv = request.form.get("cvv")
    cartlist = cc.cart_list

    while housenumber.isalpha() == True or len(housenumber) == 0:
        return render_template("checkout.html", style="alert alert-danger", result_housenumber="Sorry unvalid housenumber!")
    session["housenumber"] = housenumber

    while len(zip_code) != 5 or zip_code.isnumeric() == False:
        return render_template("checkout.html", style="alert alert-danger", result_zip_code="Your ZIP Code is to long/short! Or contains not only numeric digits!")
    session["zip_code"] = zip_code
    pcdc.add_adress_data(street, housenumber, zip_code)

    while len(credit_card_name) < 7 or " " in credit_card_name == False:
        return render_template("checkout.html", style="alert alert-danger", result_credit_card_name="Please enter a valid Name. With at least 6 digits and one blank!")
    session["credit_card_name"] = credit_card_name

    while len(credit_card_num) != 16:
        return render_template("checkout.html", style="alert alert-danger", result_credit_card_num="Wrong Card Number. The Card number consists of 16 digits!")
    session["credit_card_num"] = credit_card_num

    while credit_card_month < 1 or credit_card_month > 12:
        return render_template("checkout.html", style="alert alert-danger", result_credit_card_month="Sorry a month has to be between 1 or 12!")
    session["credit_card_month"] = credit_card_month

    while credit_card_year.isdigit() is False or int(credit_card_year) < 2021 or len(credit_card_year) == 0:
        return render_template("checkout.html", style="alert alert-danger", result_credit_card_year="Sorry the date has to contain only numbers and the year 2021!")
    session["credit_card_year"] = credit_card_year

    while len(cvv) != 3 or cvv.isdigit() is False:
        return render_template("checkout.html", style="alert alert-danger", result_cvv="CVV has to be three digits!")
    session["cvv"] = cvv

    cc.DeleteCart(add_to_cart)

    return render_template("order_closing.html", cartlist=cartlist, end_result="Thank you for your order!")

@app.route("/quiz", methods=["POST"])
def quiz():

    pass


@app.route("/show_data", methods=["POST"])
def show_data():
    user_data = ac.customer_accounts
    return render_template("show_data.html", user_data=user_data)

@app.route("/link_change_data", methods=["POST"])
def link_change_data():
    return render_template("change_data.html")

@app.route("/change_data", methods=["POST"])
def change_data():
    change_attribut = request.form.get("attribut")
    user_data = ac.customer_accounts
    value = request.form.get("value")
    username = session["username"]

    ac.update_attribut(username=username, change_attribut=change_attribut, value=value)

    if change_attribut == "firstname":
        session.pop("firstname")
        session["firstname"] = value

    elif change_attribut == "lastname":
        session.pop("lastname")
        session["lastname"] = value

    elif change_attribut == "birthday":
        session.pop("birthday")
        session["birthday"] = value

    elif change_attribut == "password":
        session.pop("password")
        session["password"] = value
    return render_template("show_data.html", user_data=user_data)

@app.route("/startpage", methods=["POST"])
def go_startpage():
    return render_template("startpage.html")

@app.route("/show_write_review", methods=["POST"])
def link_show_write_review():
    productlist = pc.product_list
    return render_template("show_write_review.html", productlist=productlist)

@app.route("/show_review", methods=["POST"])
def show_review():
 customer_review_list = crc.customer_review_list
 product_id = request.form.get("product_id")
 product_id = crc.find_product(product_id)
 return render_template("show_review.html", customer_review_list=customer_review_list, product_id=product_id)

@app.route("/link_write_review", methods=["POST"])
def link_write_review():
    session["review_id"] = request.form.get("review_id")
    return render_template("write_review.html")

@app.route("/write_review", methods=["POST"])
def write_review():
    which_product = session["review_id"]
    review_heading = request.form.get("review_heading")
    review_text = request.form.get("review_text")

    while len(review_heading) < 3:
        return render_template("write_review.html", result_heading="Please enter at least 3 digits!", style="alert alert-danger")

    while len(review_text) < 3:
        return render_template("write_review.html", result_text="Please enter at least 3 digits!", style="alert alert-danger")

    crc.new_customer_review(which_product, review_heading, review_text)
    customer_review_list = crc.customer_review_list
    product_id = crc.find_product(which_product)
    return render_template("show_review.html", customer_review_list=customer_review_list, product_id=product_id)

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return render_template("loginpage.html")

app.run(debug=True)