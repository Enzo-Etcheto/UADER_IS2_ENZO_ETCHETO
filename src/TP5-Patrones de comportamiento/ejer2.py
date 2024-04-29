from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticalOrderIterator(Iterator):

    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value

class WordsCollection(Iterable):

    def __init__(self, collection: str = "") -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: str):
        self._collection += item

if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("Uno")
    collection.add_item("Dos")
    collection.add_item("Tres")

    print("Recorrido directo:")
    for item in collection:
        print(item)

    print("\nRecorrido inverso:")
    reverse_iterator = collection.get_reverse_iterator()
    for item in reverse_iterator:
        print(item)