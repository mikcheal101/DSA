from LinkedList.LinkedList import LinkedList
from LinkedList.Node import Node
from com.reducers.ILinkedListReducer import ILinkedListReducer


class LinkedListManager:

    @staticmethod
    def perform_action(reducer: ILinkedListReducer, *args):
        return reducer.perfom_action(*args)
