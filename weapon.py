

class Weapon:
    def __init__ (self, wep_type, attack_power):
        self.wep_type = wep_type
        self.attack_power = attack_power

    def display_wep (self):
        print('Weapon: ', self.wep_type)
        print('Power: ', self.attack_power)
