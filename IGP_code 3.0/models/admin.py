from models.account import Account

class Admin(Account):

    def __init__(self, firstname, lastname, birthday, user_ID, username, password):
        Account.__init__(self, firstname, lastname, birthday, user_ID, username, password)
        self.role = "admin"

    def view_admin(self):

        print("Firstname:", self.firstname)
        print("Lastname:", self.lastname)
        print("Birthday:", self.birthday)
        print("User-ID:", self.user_ID)
        print("Username:", self.username)
        print("Password:", self.password)
        print("Role:", self.role)



