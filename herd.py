from dinosaur import Dinosaur

class Herd:
    def __init__ (self):
        self.dinos = []
        self.create_dinos()

    def create_dinos (self):
        Dino_1 = Dinosaur('Rex', 100, 25)
        Dino_2 = Dinosaur('TD', 100, 25)
        Dino_3 = Dinosaur('Raptor', 100, 25)
        self.dinos.append(Dino_1)
        self.dinos.append(Dino_2)
        self.dinos.append(Dino_3)

    def display_dinos (self):
        print("\n Your Dino Herd is: ")
        self.dinos[0].dino_info()
        self.dinos[1].dino_info()
        self.dinos[2].dino_info()

