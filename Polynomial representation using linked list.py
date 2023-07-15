#Creating polynomial equations using Linked Lists
from LinkedList import node,LinkedList

equation = [(0,9),(1,3),(2,2),(3,4)]

poly = LinkedList("Polynomial Equation")

for x in reversed(equation) :
    poly.addNode(x)

print(poly.getAllElements())
    
