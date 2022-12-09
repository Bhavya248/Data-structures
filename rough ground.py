n = int(input("Enter a number  "))
big_list = []
num = 2
for i in range(n):
    big_list.append([])
    temp = n
    while temp >= 1 :
        big_list[i].append(num+(2*(n - temp)))
        temp = temp - 1
    num = num + 1   
print(big_list)
temp = n
while temp >= 1:
    for i in range(temp-1):
        del big_list[temp-i][i]
    temp = temp - 1    
'''big_list = reversed(big_list)
for i in range(n):
    pattern = [" "for i in range(2*n + 1)]


             /'''
print(big_list)