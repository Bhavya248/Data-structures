n = int(input("Enter the value for k -->  "))
vertical_level = 1 + 2*(n-1)
horiz_length = []
for i in range(n):
    horiz_length.append(2**i)
num = 1
diamond_tree = [[] for i in range(n)]
for i in range(n) :
    for p in range(horiz_length[i]):
        diamond_tree[i].append(num)
        num=num+1
    print(" ".join(str(diamond_tree[i])))

# The next step will now shorten the tree by summing up values

base_groups = horiz_length[-1]/2
temp = base_groups
for i in range():
while temp >= 0 :

    temp = temp - 1