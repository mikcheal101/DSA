
from com.reducers.ILinkedListReducer import ILinkedListReducer
from LinkedList.Node import Node


class DeleteByValueReducer(ILinkedListReducer):
    @staticmethod
    def perfom_action(*args):
        (linked_list, value) = args
        prev = None

        current_node: Node = linked_list.head
        while current_node:
            if current_node.data == value:
                next_node = current_node.next_node
                prev.next_node = next_node
                current_node = current_node.next_node
                break
            prev = current_node
            current_node = current_node.next_node
        return linked_list
