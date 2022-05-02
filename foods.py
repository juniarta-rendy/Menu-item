from menu_item import MenuItem

class Foods(MenuItem):
    def __init__(self,name,price,kal):
        super().__init__(name,price)
        self.kal = kal
        
    def info(self):
        return self.name +': ' +str(self.price) +'$' +' (' +str(self.kal) +'kkal)'
    
    def calorie_info(self):
        pass
        