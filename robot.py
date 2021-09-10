from weapon import Weapon 

class Robot:
    def __init__ (self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        
              
    
    def robot_info (self):
        print('Robots Name: ', self.name)
        print('Robots Health: ', self.health)
        print('Robots Weapon: ', self.weapon.wep_type)
        print('Attack Power: ', self.weapon.attack_power)
        

    def robo_attack (self, dinosaur):
        dinosaur.health -= self.wep_power

    


    