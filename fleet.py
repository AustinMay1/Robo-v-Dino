from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_robots()

    def create_robots (self):
        robot_1 = Robot('Gold', 100, Weapon('Sword', 50))
        robot_2 = Robot('Silver', 100, Weapon('Dagger', 25))
        robot_3 = Robot('Platinum', 100, Weapon('Scythe', 100))
        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)
        
    def display_robots (self):
        print("\n Your Robot Fleet is: ")
        self.robots[0].robot_info()
        self.robots[1].robot_info()
        self.robots[2].robot_info()



