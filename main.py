from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedListManager import LinkedListManager
import random

if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(20):
        new_number = random.randint(1, 999)
        LinkedListManager.insert(linked_list=linked_list, data=new_number)

    # print the linked list
    LinkedListManager.print_list(linked_list)

    
