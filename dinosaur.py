

class Dinosaur:
    def __init__ (self, name, health, attack) :
        self.name = name
        self.health = health
        self.att_power = attack 

    def dino_info (self):
        print('Your Dinos name is: ', self.name)
        print('Your Dinos health is: ', self.health)
        print('Your Dinos attack power is: ', self.att_power)
    

    def attack (self):
        robot.health -= self.att_power
