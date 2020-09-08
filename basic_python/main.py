

import my_structs


list = my_structs.List()
list.addNode(4)
list.addNode(3)
list.addNode(2)
list.addNode(1)

#list.printList()

#print(list.getAtIndex(1))

g = my_structs.Graph()
g.addNode("Bucharest")
g.addNode("Giurgiu")
g.addNode("Sibiu")
g.addNode("Constanta")
g.addBiPath("Giurgiu", "Bucharest", 50)
g.addPath("Sibiu", "Giurgiu", 34)

g.printGraph()
