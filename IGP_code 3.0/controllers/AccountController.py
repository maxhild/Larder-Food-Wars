from models.admin import Admin
from models.customer import Customer

class AccountController:

    customer_accounts = []
    admin_list = []

    def create_customer_account(self, firstname, lastname, birthday, user_ID, username, password):
        individual_customer = Customer(firstname, lastname, birthday, user_ID, username, password)
        self.customer_accounts.append(individual_customer)

    def add_admins(self, firstname, lastname, birthday, user_ID, username, password):
        individual_admin = Admin(firstname, lastname, birthday, user_ID, username, password)
        self.admin_list.append(individual_admin)

    def login(self, username, password):

        for admin in self.admin_list:

            if admin.username == username and admin.password == password:

                return 'admin'

        for customer in self.customer_accounts:

            if customer.username == username and customer.password == password:

                return "customer"

            else:

                return False

    def print_customer_accounts(self):
        for customer in self.customer_accounts:
            print("--------------")
            customer.view_customer()

    def print_admin_accounts(self):
        for admin in self.admin_list:
            admin.view_admin()

    def find_account(self, username):
        for account in self.customer_accounts:
            if account.username == username:
                return account

    def update_attribut(self, username, change_attribut, value):
        account = self.find_account(username)

        if account is not None:

            account.change_customer_account(change_attribut, value)

ac = AccountController()

ac.add_admins(firstname="Mario", lastname="von Bassen", birthday="25.08.1999", user_ID="123456", username="Progamer", password="12993409")
