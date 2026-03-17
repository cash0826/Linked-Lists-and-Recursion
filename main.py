from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    llexample = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    llexample.insert_at_front(1)
    llexample.insert_at_front(2)
    llexample.insert_at_front(3)
    llexample.insert_at_front(4)
    
    # TODO: 3) Display the list to verify insertion
    llexample.display()

    # TODO: 4) Call recursive_sum and print the result
    print(llexample.recursive_sum())

    # TODO: 5) Call recursive_search with a target and print result
    print(f"Recursive_sarch: {llexample.recursive_search(3)} ")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print(llexample.recursive_reverse())

# 