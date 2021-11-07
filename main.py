from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedListManager import LinkedListManager
import random
from com.reducers.linkedListReducer.DeleteByValueReducer import DeleteByValueReducer

from com.reducers.linkedListReducer.InsertReducer import InsertReducer
from com.reducers.linkedListReducer.PrintReducer import PrintReducer

if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(3):
        new_number = random.randint(1, 999)
        linked_list = LinkedListManager.perform_action(
            InsertReducer, linked_list, new_number)
    

    LinkedListManager.perform_action(PrintReducer, linked_list)

    # print the linked list
    LinkedListManager.perform_action(PrintReducer, linked_list)
    new_number = 300000
    linked_list = LinkedListManager.perform_action(
            InsertReducer, linked_list, new_number)
    LinkedListManager.perform_action(PrintReducer, linked_list)

    LinkedListManager.perform_action(DeleteByValueReducer, linked_list, 300000)
    
    LinkedListManager.perform_action(PrintReducer, linked_list)