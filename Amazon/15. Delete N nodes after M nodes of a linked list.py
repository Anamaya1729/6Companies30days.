class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        temp, mul, count, x = head, 1, 1, N
        
        while temp and temp.next:
            if count == M*mul:
                prev = temp
                while x > 0 and temp.next:
                    temp = temp.next
                    x-= 1
                prev.next = temp.next
                mul += 1
                x = N
            count += 1
            temp = temp.next

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ") 
            temp = temp.next
        print("")


if __name__=='__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        m,p = list(map(int, input().strip().split()))
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        Solution().skipMdeleteN(llist.head, m, p)
        llist.printList()
        t -= 1
