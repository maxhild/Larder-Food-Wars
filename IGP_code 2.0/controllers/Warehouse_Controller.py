from models.warehouse import Warehouse

class WarehouseController:

    stock_list = []

    def Inventory(self):

        stock = Warehouse()
        self.stock_list.append(stock)

    def print_stock(self):

        for products in self.stock_list:

            products.Warehouse.view_stock()

WarehouseController().print_stock()