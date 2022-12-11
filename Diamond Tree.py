n = int(input("Enter the value for k -->  "))
vertical_level = 1 + 2*(n-1)
horiz_length = []
for i in range(n):
    horiz_length.append(2**i)
num = 1
diamond_tree = [[] for i in range(n)]
for i in range(n):
    for p in range(horiz_length[i]):
        diamond_tree[i].append(str(num))
        num = num+1
    print(" ".join(diamond_tree[i]))

# The next step will now shorten the tree by summing up values
diamond_tree = diamond_tree[-1]
base_groups = int(horiz_length[-1]/2)
short = [[] for i in range(base_groups)]
for i in range((base_groups)):
    short[i].append(diamond_tree[2*i])
    short[i].append(diamond_tree[2*i+1])
