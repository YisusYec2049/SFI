# Here We will be stored logic of product.
from SFI import Data


class Product:
    def __init__(self, name=None, cost=None, pvp=None, cod=None, cant=None, vendor=None, date=None):
        self.name = name
        self.cost = cost
        self.pvp = pvp
        self.cod = cod
        self.cant = cant
        self.vendor = vendor
        self.date = date

    def create_product(self, name, cost, pvp):
        self.name = name
        self.cost = cost
        self.pvp = pvp

        try:
            self.cost = int(self.cost)
            self.pvp = int(self.pvp)

        except:
            print('Cost and sale price must be numbers')
            exit()
        self.cod = 1
        self.cod = str(self.cod)
        for i in Data.products:
            if i['cod'] == self.cod:
                self.cod = int(self.cod)
                self.cod += 1
                self.cod = str(self.cod)
        newproduct = {
            'cod': self.cod,
            'name': self.name,
            'cost': self.cost,
            'pvp': self.pvp,
            'stock': '0'
        }

        Data.products.append(newproduct)
        return Data.products

    def validate_product(self, cod, name):
        self.cod = cod
        self.name = name

        try:
            self.cod = int(self.cod)
        except:
            print("The cod must be numbers")
            exit()
        self.cod = str(self.cod)
        for i in Data.products:
            if i['name'] == self.name and i['cod'] == self.cod:
                return Data.products
        return 'Error'

    def add_stock(self, cant, vendor, date):
        self.cant = cant
        self.vendor = vendor
        self.date = date
        try:
            self.cant = int(self.cant)
        except:
            print("The cant must be numbers")
            exit()

        if not self.validate_product(input('cod '), input('name ')):
            print('Error')
            exit()
        return self.find_stock(self.name, self.cod)

    def find_stock(self, n, c):
        a = None
        for i in Data.products:
            if i['cod'] == c and i['name'] == n:
                a = i['stock']
                a = int(a)
        return a

    def stock_total(self, x, y):
        stocktotal = x + y
        stocktotal = str(stocktotal)
        return stocktotal


test = Product()
# test.create_product(input('name '), input('cost '), input('pvp '))
# test.validate_product(input('cod '), input('name '))
test.add_stock(input('cant '), input('vendor '), input('date '))
