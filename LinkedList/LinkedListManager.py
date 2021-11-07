from LinkedList.LinkedList import LinkedList
from LinkedList.Node import Node


class LinkedListManager:

    @staticmethod
    def insert(linked_list: LinkedList, data: int):
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


    @staticmethod
    def print_list(linked_list: LinkedList):
        current_node = linked_list.head
        final_string = ["[+] Linked List: "]

        # tranverse the list 
        while current_node.next_node:
            final_string.append(" -> ({})".format(current_node.data))
            current_node = current_node.next_node

        print("".join(final_string))
