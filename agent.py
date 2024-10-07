#Création des agents de la simulation
import random
# Définition de la classe
class agent:
    def __init__(self, anger, speed, view):
        self.anger = anger
        self.speed = 1
        self.view = 2
        self.XP = 20

    def RandomWalk(self):
        random_int = random.randint(1, 4)
        return random_int


'''
    def afficher_info(self):
        return f"Colère : {self.anger}, Prix : {self.prix}"


# Instanciation de l'objet
ma_voiture = agent(2020)

# Utilisation de l'objet
print(ma_voiture.afficher_info())

print(ma_voiture.prix)

'''