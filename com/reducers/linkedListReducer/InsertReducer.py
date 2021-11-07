from LinkedList.Node import Node
from com.reducers.ILinkedListReducer import ILinkedListReducer


class InsertReducer(ILinkedListReducer):
    @staticmethod
    def perfom_action(*args):
        (linked_list, data) = args
        # create a new node to hold the data
        new_node = Node(data)

        # if the linked list is null, make the new_node the head
        if linked_list.head:
            # tranverse the list and add the node
            last_node = linked_list.head
            while last_node.next_node:
                last_node = last_node.next_node
            last_node.next_node = new_node
        else:
            linked_list.head = new_node

        return linked_list