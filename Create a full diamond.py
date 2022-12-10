n = int(input("Enter a number  "))
istyp = str(input("Full Diamond(F) or inverse diamond(I)"))
def diamond(n,istyp): 
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
    if istyp == "F" :    
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
    else :
         pattern = ["*" for i in range(2*n+2)]
         for i in range(len(lista)-1, -1, -1):
            for m in lista[i]:
                pattern[m] = ""
            print(" ".join(pattern))
            pattern = ["*" for i in range(2*n+2)]
         for i in range(len(lista)):
            for m in lista[i]:
                pattern[m] = ""
            print(" ".join(pattern))
            pattern = ["*" for i in range(2*n+2)]
diamond(n,istyp)