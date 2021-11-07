from abc import ABC


class ILinkedListReducer(ABC):
    @staticmethod
    def perfom_action(*args):
        """ method to be fired by a linked list reducer """
        pass