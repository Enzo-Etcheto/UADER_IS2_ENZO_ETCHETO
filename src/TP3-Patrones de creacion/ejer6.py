from abc import ABC, abstractmethod
import time
from datetime import datetime
import copy
import os

class Prototype(ABC):
    def __init__(self):
        time.sleep(2)  
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    @abstractmethod
    def clone(self):
        pass

class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.charisma = 30

    def clone(self):
        return copy.deepcopy(self)

class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        self.stamina = 60

    def clone(self):
        return copy.deepcopy(self)

class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        self.mana = 100

    def clone(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    os.system("clear")
    print("Ejemplo de taller para patron prototipo")

    dt = datetime.now()
    print('Comienza creando un objeto Shopkeeper NPC: ', dt)
    shopkeeper = Shopkeeper(180, 22, 5, 8)

    dt = datetime.now()
    print('Finaliza la creación del objeto Shopkeeper NPC: ', dt)
    print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

    dt = datetime.now()
    print('Instanciando ahora trader: ', dt)
    for i in range(5):
        shopkeeper = Shopkeeper(180, 22, 5, 8)
        dt = datetime.now()
        print(f'Creo Shopkeeper NPC {i} at: ', dt)

    dt = datetime.now()
    print('Finalizo de crear el grupo trader: ', dt)

    dt = datetime.now()
    print('Puedo hacerlo masivamente con 10 NPCs: ', dt)
    shopkeeper_template = Shopkeeper(180, 22, 5, 8)
    warrior_template = Warrior(185, 22, 4, 21)
    mage_template = Mage(172, 65, 8, 15)
    
    def create_clones(obj, num_clones):
        if num_clones == 0:
            return
        clone = obj.clone()
        create_clones(clone, num_clones - 1)

    for i in range(3):
        shopkeeper_clone = shopkeeper_template.clone()
        warrior_clone = warrior_template.clone()
        mage_clone = mage_template.clone()
        create_clones(shopkeeper_clone, 6)
        create_clones(warrior_clone, 6)
        create_clones(mage_clone, 6)
        dt = datetime.now()
        print(f'Finaliza la creacion de tripletes mediante clone {i} at: ', dt)

    dt = datetime.now()
    print('Finalizó la creacion de la población NPC: ', dt)