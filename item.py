class Item():
    def __init__(self):
        self.item_name = None
        self.description = None
        self.item = None
    

    def set_item_name(self, item_new_name):
        self.item_name = item_new_name

    def get_name(self):
        print(self.item_name)
    
    def set_item_description(self, new_item):
        self.description = new_item
    
    def get_item_description(self):
        print(self.description)
    
    def set_item(self, the_item): #creating the key object for task 5
        self.item = the_item
        print(self.item)
    
  

