
class NameWithCost:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost


class Graph:
    def __init__(self):
        self.nodes = {}

    def addNode(self, value):
        self.nodes[value] = List()

    def addPath(self, src_name, dest_name, cost=1):
        new_dest = NameWithCost(dest_name,cost)
        self.nodes[src_name].addNode(new_dest)



    def addBiPath(self, src_name, dest_name, cost=1):
        self.addPath(src_name, dest_name, cost)
        self.addPath(dest_name, src_name, cost)

    def printGraph(self):
        for i in self.nodes:
            print(i, ":")
            self.printGraphNode(self.nodes[i])

    def printGraphNode(self, node):
        tmp = node

        if tmp.value != None:
            while tmp != None:
                print("\t", tmp.value.name, tmp.value.cost)
                tmp = tmp.next 
        



class List:

    def __init__(self, value = None):
        self.value = value
        self.next = None

    def addNode(self, value):

        tmp = self

        if tmp.value != None:
            while tmp.next != None:
                tmp = tmp.next
            new_node = List(value)
            tmp.next = new_node
        else:
            self.value = value

    def printList(self):
        tmp = self
        while tmp != None:
            print(tmp.value)
            tmp = tmp.next

    def getAtIndex(self, index):
        tmp = self
        i = 0
        while tmp != None and i != index:
            tmp = tmp.next
            i+=1

        if i != index:
            print("Index is too big")
            return 0
        else:
            return tmp.value


'''
class Tree:
    def __init__(self):
        pass
class TreeNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value
'''


# Define a function
def world():
    print("Hello, World!")