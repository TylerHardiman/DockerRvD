

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 25

    def attack(self, robot, robot_list):
        robot.health -= self.attack_power
        print()
        print(f'Dinosaur {robot.name} was attacked by robot {self.name} and did {self.attack_power} damage')
        print(f'{robot.name} has {robot.health} remaining health')
        print()
        if robot.health <= 0:
            robot_list.remove(robot)