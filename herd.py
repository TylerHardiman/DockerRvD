from dino import Dinosaur
class Herd:
    
    def __init__(self):
        self.dinos = []
        self.create_herd()

    def create_herd(self): 
        dinosaur_one = Dinosaur("Smash")
        dinosaur_two = Dinosaur("gnashhh")
        dinosaur_three = Dinosaur("crash")

        self.dinos.append(dinosaur_one)
        self.dinos.append(dinosaur_two)
        self.dinos.append(dinosaur_three)
