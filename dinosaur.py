class Dinosaur:
    def __init__ (self) :
        self.name = ' '
        self.health = 100
        self.att_power = 25 

    def set_dino_name (self):
        self.name = input("Please enter a name for your Dinosaur.")
        print = ("You have chosen the name: ",self.name, " for your Dinosaur")

    def check_health_dino (self):
        print("Your dinosaurs current health is: ", self.health)

    def att_power_dino (self):
        print("Your dinosaurs attack power is: ", self.att_power)

    