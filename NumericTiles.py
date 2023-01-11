n =int(input("Enter Value"))
length=2*n-1
pattern=[["" for i in range(length)] for i in range(length)]
space=0
def create(l,s):
    if s==n:
        return None
    for i in range(l):
        if i in (0,l-1):
            for p in range(l):
                pattern[i+s][p+s]=n-s
        else:
            pattern [i+s][0+s]=n-s
            pattern [i+s][l-1+s]=n-s
            
    l=l-2
    s =s +1
    create(l,s)

create(length,space)
for i in pattern:
    print("".join(i))
