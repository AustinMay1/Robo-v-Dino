class Robot:
    def __init__ (self):
        self.name = ' '
        self.health = 100
              
    def set_name (self):
        self.name = input("Please choose a name for your robot.")
        print("Robot name: ", self.name)

    def avail_health (self):
        print("Your robots current health is: ", self.health)

class Weapon:
    def __init__ (self):
        self.weapon = 'Sword'
        self.attack_power = 25

    def display_weapon (self):
        print("Your current weapon is: ",self.weapon," with an attack power of: ",self.attack_power)

    


    