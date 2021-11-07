from LinkedList.Node import Node


class LinkedList:
    def __init__(self) -> None:
        self._head = None

    @property
    def head(self):
        return self._head


    @head.setter
    def head(self, value: Node):
        self._head = value