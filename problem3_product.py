class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getTotalPrice(self):
        return self.price * self.quantity


product = Product("Laptop", 1000, 2)
print(product.getTotalPrice())
