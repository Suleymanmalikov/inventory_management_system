from product import Product


class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product):
        exist, existing_product = self.check_name(product.get_name())
        if not exist:
            self.products.append(product)
            return f"\n{product.name} added to Inventory\n"
        else:
            return f"\n{product.name} already exist"
    
    def view_inventory(self):
        for product in self.products:
            print(product)
    
    def check_name(self, name):
        for product in self.products:
            if(product.get_name() == name):
                return (True, product)
        return (False, None)
    
    def remove_product_by_name(self, name):
        res, product = self.check_name(name)
        if res and product:
            self.products.remove(product)
            return f"{name} has successfully removed\n"
        else:
            return f"{name} not found in inventory\n"

    
    def restock_product_by_name(self, name, new_quantity):
        res, product = self.check_name(name)
        if res and product:
            product.set_quantity(new_quantity)
            return f"New Quantity for {product.get_name()} is ({product.get_quantity()})"
        
    def show_total_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.get_price() * product.get_quantity()
        return total_value
    


        