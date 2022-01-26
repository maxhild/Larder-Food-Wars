class PaymentCustomerData():

    def __init__(self,street, housenumber, zip_code):
        self.street = street
        self.housenumber = housenumber
        self.zip_code = zip_code

    def show_whole_payment_customer(self):

        print("Street:", self.street)
        print("Housenumber:", self.housenumber)
        print("ZIP Code:", self.zip_code)

