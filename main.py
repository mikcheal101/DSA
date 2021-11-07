from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedListManager import LinkedListManager
import random

from com.reducers.linkedListReducer.InsertReducer import InsertReducer
from com.reducers.linkedListReducer.PrintReducer import PrintReducer

if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(20):
        new_number = random.randint(1, 999)
        linked_list = LinkedListManager.perform_action(
            InsertReducer, linked_list, new_number)
            
    # print the linked list
    LinkedListManager.perform_action(PrintReducer, linked_list)