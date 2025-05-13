# Node class: represents a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data      # The value stored in the node
        self.next = None      # Pointer to the next node (None by default)


# LinkedList class: manages the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            # If list is empty, new node becomes the head
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Add new node at the end

    # Insert a new node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point to the old head
        self.head = new_node       # New node becomes the head

    # Insert a node at a specific index (0-based)
    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        count = 0
        # Traverse to the node just before the desired index
        while current and count < index - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of range")
        else:
            new_node.next = current.next
            current.next = new_node

    # Delete a node at a specific index (0-based)
    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index == 0:
            self.head = self.head.next  # Remove the head
            return
        current = self.head
        count = 0
        # Traverse to the node just before the one to delete
        while current and count < index - 1:
            current = current.next
            count += 1
        # If index is out of range
        if current is None or current.next is None:
            print("Index out of range")
        else:
            current.next = current.next.next  # Bypass the node to delete

    # Search for a value in the list and return its index
    def search(self, value):
        current = self.head
        index = 0
        # Traverse the list to find the value
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1  # Value not found

    # Display all node values in the list
    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
        else:
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")  # End of list


# Example usage (can be removed during testing)
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_start(5)
    ll.insert_at_end(20)
    ll.insert_at_index(1, 15)   # List becomes: 5 -> 15 -> 10 -> 20
    ll.display()
    print("Index of 10:", ll.search(10))  # Output: 2
    ll.delete_at_index(2)  # Deletes node with value 10
    ll.display()
