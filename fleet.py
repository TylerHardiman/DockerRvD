from robot import Robot
class Fleet:
    
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_one = Robot("Clank")
        robot_two = Robot("Power Rangers Morph")
        robot_three = Robot("Baymax")

        self.robots.append(robot_one)
        self.robots.append(robot_two)
        self.robots.append(robot_three)


       
                
