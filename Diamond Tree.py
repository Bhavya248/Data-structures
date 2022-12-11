import time
t1 = time.perf_counter()
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
while n > 0:
    short = []
    for i in range(int(len(diamond_tree)/2)):
        short.append(str(int(diamond_tree[2*i]) + int(diamond_tree[2*i+1])))
    print(" ".join(short))
    diamond_tree = short
    n = n - 1
    del short
t2 = time.perf_counter()
print("The program took ",(t2-t1)*1000,'Ms to execute')