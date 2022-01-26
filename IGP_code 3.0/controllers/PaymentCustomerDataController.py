from models.paymentcustomerdata import PaymentCustomerData

class PaymentCustomerDataController:

    whole_customer_data_list = []

    def add_adress_data(self, street, housenumber, zip_cod):
        added_adress = PaymentCustomerData(street, housenumber, zip_cod)
        self.whole_customer_data_list.append(added_adress)

    def print_customer_payment_data(self):
        for whole_customer in self.whole_customer_data_list:
            print("--------------")
            print("Invoice Data")
            whole_customer.show_whole_payment_customer()

