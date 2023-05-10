from random import randint

class Dice:

    def __init__(self,sides):
        self.sides = sides
    
    def roll_dice(self):
        print(randint(1, self.sides))
    

six_die = Dice(6)
six_die.roll_dice()

ten_die = Dice(10)
ten_die.roll_dice()

twelve_die = Dice(20)
twelve_die.roll_dice()
        
