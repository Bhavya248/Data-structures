try :
   n = int(input('provide levels for pattern -->  '))
except ValueError :
    print("Enter an integral value for n")
    n = int(input('provide levels for pattern'))

writeable_spaces = 2*n + 1
star_levels=[]
for i in range(0,n):
    star_levels.append(1+2*i)    
for i in range(0,n):
        whites = n-i-1
        pattern = []
        for p in range(whites,0,-1):
            pattern.append(" ")
            le = [" " for i in range(1+2*(i+1))]
        pattern.append("*"*star_levels[i])
        for r in range(whites,0,-1):
            pattern.append(" ") 
        for s in pattern:
            print(s,end="")
        print("",end="\n")
        pattern=[]    
