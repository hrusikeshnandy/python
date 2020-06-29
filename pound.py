import random
class Coin:
    def __init__(self,rare = False,clean = True,head = True,**kwargs):

        for key,value in kwargs(item):
            setattr(self,key,value)
            

        self.rare = rare
        self.clean = clean
        self.head = head
        if self.rare:
            self.price = self.original_value *1.25
        else:
            self.price = self.original_value

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("coin spent")

    def flip(self):
        head_options=[True,False]
        choice = random.choice(head_options)
        self.choice = choice
        

class Pound(Coin):
    def __init__(self):
        data={
            "original_value":0.01,
            "clean_colour":"bronze",
            "rusty_colour":"brownish",
            }
    super().__init__(**data)
        
        


    
