n = int(input("Enter a number  "))
big_list = []
num = 2
for i in range(1,n+1):
    big_list.append([])
    for p in range(1,n+1):
        if len(big_list) > 1:
            big_list[i].append(num*p)
            pass
            
