class Fuselaje:
    shape = None

class Turbina:
    horsepower = None

class Ala:
    size = None

class TrenAterrizaje:
    type = None

class BuilderAvion:
    def getFuselaje(self): pass
    def getTurbina(self): pass
    def getAla(self): pass
    def getTrenAterrizaje(self): pass

class AvionComercialBuilder(BuilderAvion):
    def getFuselaje(self):
        fuselaje = Fuselaje()
        fuselaje.shape = "Avion comercial"
        return fuselaje

    def getTurbina(self):
        turbina = Turbina()
        turbina.horsepower = 10000
        return turbina

    def getAla(self):
        ala = Ala()
        ala.size = "Grande"
        return ala

    def getTrenAterrizaje(self):
        tren = TrenAterrizaje()
        tren.type = "Con ruedas"
        return tren

class DirectorAvion:
    def setBuilder(self, builder):
        self.builder = builder

    def getAvion(self):
        avion = Avion()
        avion.fuselaje = self.builder.getFuselaje()
        avion.turbina = self.builder.getTurbina()
        avion.ala = self.builder.getAla()
        avion.tren_aterrizaje = self.builder.getTrenAterrizaje()
        return avion

class Avion:
    def __init__(self):
        self.fuselaje = None
        self.turbina = None
        self.ala = None
        self.tren_aterrizaje = None

    def specification(self):
        print("Fuselaje: %s" % (self.fuselaje.shape))
        print("Turbina: %d horsepower" % (self.turbina.horsepower))
        print("Ala: %s" % (self.ala.size))
        print("Tren de Aterrizaje: %s" % (self.tren_aterrizaje.type))

def main():
    avion_builder = AvionComercialBuilder()
    director = DirectorAvion()
    director.setBuilder(avion_builder)
    avion = director.getAvion()
    avion.specification()

if __name__ == "__main__":
    main()