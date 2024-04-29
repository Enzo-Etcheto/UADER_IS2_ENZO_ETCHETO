import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        if len(self.history) < 4:
            self.history.append(Memento(self.file, self.content))
        else:
            self.history.pop(0)
            self.history.append(Memento(self.file, self.content))

    def undo(self, num_states):
        if num_states >= len(self.history):
            print("No hay suficientes estados almacenados para deshacer")
            return
        for _ in range(num_states):
            memento = self.history.pop()
            self.file = memento.file
            self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, num_states=1):
        writer.undo(num_states)

if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la version anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")

    print("Se invoca al <undo>")
    caretaker.undo(writer)

    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> con recuperación de los 2 estados anteriores")
    caretaker.undo(writer, 2)

    print("Se muestra el estado actual")
    print(writer.content + "\n\n")