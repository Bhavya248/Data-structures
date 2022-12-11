# Python3 program to create the diamond
# like structure of Binary Tree
# for a given value of K

# A Tree node
import time 
t1 = time.perf_counter()
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Utility function to create a new node


def createNewNode(value):

    temp = Node(value)
    return temp

# Utility function to create the diamond
# like structure of Binary tree


def createStructureUtil(qu, k):

    num = 1
    level = k - 1

    # Run the outer while loop
    # and create structure up to
    # the k levels
    while (level != 0):

        level -= 1

        qsize = len(qu)

        # Run inner while loop to
        # create current level
        while (qsize != 0):

            qsize -= 1
            temp = qu[0]
            qu.pop(0)
            num += 1

            # Create left child
            temp.left = createNewNode(num)
            num += 1

            # Create right child
            temp.right = createNewNode(num)

            # Push the left child into
            # the queue
            qu.append(temp.left)

            # Push the right child into
            # the queue
            qu.append(temp.right)

    num += 1

    # Run the while loop
    while (len(qu) > 1):

        # Pop first element from the queue
        first = qu[0]
        qu.pop(0)

        # Pop second element from the queue
        second = qu[0]
        qu.pop(0)

        # Create diamond structure
        first.right = createNewNode(first.data + second.data)
        second.left = first.right

        # Push the node into the queue
        qu.append(first.right)


# Function to print the Diamond
# Structure of Binary Tree
def printLevelOrder(root, k):

    # Base Case
    if (root == None):
        return

    # Create an empty queue
    qu = []

    # Enqueue Root and initialize height
    qu.append(root)
    level = k - 1

    # while loop to print the element
    # up to the (k - 1) levels
    while (level != 0):

        level -= 1

        qsize = len(qu)

        while (qsize != 0):

            qsize -= 1

            temp = qu[0]
            qu.pop(0)
            print(temp.data, end=' ')

            # Enqueue left child
            if (temp.left != None):
                qu.append(temp.left)

            # Enqueue right child
            if (temp.right != None):
                qu.append(temp.right)
        print()

    # Loop to print the element
    # rest all level except last
    # level
    while (len(qu) > 1):

        qsize = len(qu)

        while (qsize != 0):

            first = qu[0]
            qu.pop(0)
            second = qu[0]
            qu.pop(0)
            print(str(first.data)+' '+str(second.data), end=' ')
            qu.append(first.right)
            qsize = qsize - 2
        print()

    # Print the last element
    first = qu[0]
    qu.pop(0)
    print(first.data)

# Function to create the
# structure


def createStructure(k):

    qu = []
    root = createNewNode(1)
    qu.append(root)

    # Utility Function call to
    # create structure
    createStructureUtil(qu, k)
    printLevelOrder(root, k)


# Driver code
if __name__ == '__main__':

    k =10

    # Print Structure
    createStructure(k)

    # This code is contributed by rutvik_56
t2 = time.perf_counter()
print((t2-t1)*1000)