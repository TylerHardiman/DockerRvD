


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 25
    
        
    def attack(self, dinosaur, dino_list):
        dinosaur.health -= self.weapon
        print()
        print(f'Dinosaur {dinosaur.name} was attacked by robot {self.name} and did {self.weapon} damage')
        print(f'{dinosaur.name} has {dinosaur.health} remaining health')
        print()
        if dinosaur.health <= 0:
            dino_list.remove(dinosaur)