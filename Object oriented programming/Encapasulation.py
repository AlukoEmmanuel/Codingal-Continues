class Computer:

    def __init__(self, a,b):
        self.maxprice = a
        self.price = b

    def sell(self):
        print("Selling Price:",self.maxprice)
        print("Actual Price:",self.price)

    def setMaxPrice(self, price):
        self.maxprice = price

c = Computer(1000,800)
c.sell()

# change the price
c.maxprice = 2000
c.price = 1000
c.sell()

# using setter function
c.setMaxPrice(2000)
c.sell()