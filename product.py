class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price:,} ({self.quantity} in stock)"

    
    def set_name(self, name):
        self.name = name
        return f"Name updated to {self.name}"

    def get_name(self):
        return self.name
    
    
    def set_price(self, price):
        self.price = price
        return f"Price updated to {self.price:,}"

    def get_price(self):
        return self.price
    
    
    def set_quantity(self, quantity):
        self.quantity = quantity
        return f"Quantity updated to {self.quantity}"

    def get_quantity(self):
        return self.quantity


    def total_value(self):
        return self.get_price() * self.get_quantity()




