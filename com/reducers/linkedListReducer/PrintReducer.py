from com.reducers.ILinkedListReducer import ILinkedListReducer


class PrintReducer(ILinkedListReducer):
    @staticmethod
    def perfom_action(*args):
        linked_list = args[0]
        current_node = linked_list.head
        final_string = ["[+] Linked List: "]

        # tranverse the list 
        while current_node:
            final_string.append(" -> ({})".format(current_node.data))
            current_node = current_node.next_node

        print("".join(final_string))
