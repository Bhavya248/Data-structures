import time
n = int(input('provide levels for pattern --> '))
t1 = time.perf_counter()
writeable_spaces = 2*n + 1
star_levels = []
for i in range(0, n):
    star_levels.append(1+2*i)
    whites = n-i-1
    pattern = []

    for p in range(whites, 0, -1):
        pattern.append(" ")
        
    pattern.append("*"*star_levels[i])

    for r in range(whites, 0, -1):
        pattern.append(" ")
    
    for s in pattern:
        print(s, end="")
    print("", end="\n")
    pattern = []
t2 = time.perf_counter()
print("The program took ",(t2-t1)*1000,'Ms to execute') 