from menu_item import MenuItem

class Drinks(MenuItem):
    def __init__(self,name,price,vol):
        super().__init__(name,price)
        self.vol = vol
    
    def info(self):
        return self.name +': ' +str(self.price) +'$' +' (' +str(self.vol) +'ml)'
        