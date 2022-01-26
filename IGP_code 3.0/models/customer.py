from models.account import Account
from flask import session

#Die Klasse Customer unterscheidet sich von der Klasse Admin in soweit, dass sie einen anderen Wert in "role" zugeordnet bekommt

class Customer(Account):

    def __init__(self, firstname, lastname, birthday, user_ID, username, password):
        super(Customer, self).__init__(firstname, lastname, birthday, user_ID, username, password)
        #Hier wird der Customer eindeutig der Rolle Customer zugeordnet
        self.role = "customer"

    #Diese Methode dient nur dazu den Customer auszugeben
    def view_customer(self):

            print("Firstname:", self.firstname)
            print("Lastname:", self.lastname)
            print("Birthday:", self.birthday)
            print("User-ID:", self.user_ID)
            print("Username:", self.username)
            print("Password:", self.password)
            print("Role:", self.role)

    #werden die Daten des Customers verändert wird mit dieser Methode überprüft welcher Wert geändert werden soll
    def change_customer_account(self, change_attribut, new_value):

        if change_attribut == "firstname":

            self.firstname = new_value

        elif change_attribut == "lastname":

            self.lastname = new_value

        elif change_attribut == "birthday":

            self.birthday = new_value

        elif change_attribut == "username":

            self.username = new_value

        elif change_attribut == "password":

            self.password = new_value

