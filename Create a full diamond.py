import time
n = int(input("Enter a number  "))
def diamond(n):
    t1 = time.perf_counter() 
    lista = [[]for i in range(n)]
    num = 2
    for i in range(len(lista)):
        count = n - i
        temp = 0
        while count >= 1:
            lista[i].append(num + (2*(temp)))
            count = count - 1
            temp = temp + 1
        num = num + 1
    pattern = [" " for i in range(2*n+3)]
    for i in range(len(lista)-1, -1, -1):
            for m in lista[i]:
                pattern[m] = "*"
            print(" ".join(pattern))
            pattern = [" " for i in range(2*n+3)]
    for i in range(len(lista)):
        for m in lista[i]:
            pattern[m] = "*"
        print(" ".join(pattern))
        pattern = [" " for i in range(2*n+3)]
    t2 = time.perf_counter()
    print("The program took ",(t2-t1)*1000,'Ms to execute')    
diamond(n)