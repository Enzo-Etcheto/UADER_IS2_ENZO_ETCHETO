from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: str = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self, state: str) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = state 

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass

class ObservadorConcretoA(Observer):
    _id: str = "ABCD"

    def update(self, sujeto: Subject) -> None:
        if sujeto._state == self._id:
            print(f"ObservadorConcretoA: Recibido ID coincidente: {self._id}")


class ObservadorConcretoB(Observer):
    _id: str = "WXYZ"

    def update(self, sujeto: Subject) -> None:
        if sujeto._state == self._id:
            print(f"ObservadorConcretoB: Recibido ID coincidente: {self._id}")


class ObservadorConcretoC(Observer):
    _id: str = "MNOQ"

    def update(self, sujeto: Subject) -> None:
        if sujeto._state == self._id:
            print(f"ObservadorConcretoC: Recibido ID coincidente: {self._id}")


class ObservadorConcretoD(Observer):
    _id: str = "PQRS"

    def update(self, sujeto: Subject) -> None:
        if sujeto._state == self._id:
            print(f"ObservadorConcretoD: Recibido ID coincidente: {self._id}")


if __name__ == "__main__":

    sujeto = ConcreteSubject()

    observador_a = ObservadorConcretoA()
    sujeto.attach(observador_a)

    observador_b = ObservadorConcretoB()
    sujeto.attach(observador_b)

    observador_c = ObservadorConcretoC()
    sujeto.attach(observador_c)

    observador_d = ObservadorConcretoD()
    sujeto.attach(observador_d)

    ids = ["ABCD", "EFGH", "IJKL", "WXYZ", "MNOQ", "PQRS", "TUVW", "XYZA"]

    print("IDs emitidos:")
    for id in ids:
        print(id)
        sujeto.some_business_logic(id)