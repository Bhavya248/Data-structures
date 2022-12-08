# full diamond pattern
n = int(input("Enter a number for the pattern -->  "))
fields = 2*n+1
pattern = [" "for i in range(fields)]
count = 0 
temp = n
if n % 2 == 0 :
        count = int(n / 2)
else: 
    count = int((n + 1) / 2)        
for i in range(count,0,-1):
    inex_a = int((fields+1)/2)
    inex_b = int((fields+1)/2)
    print(pattern)
    while temp > 0 :
        pattern[inex_a]="*"
        pattern[inex_b]="*"
        print(" ".join(pattern))
        inex_a = inex_a + 1
        inex_b = inex_b - 1
        pattern = [" "for i in range(2*n+1)]
        temp = temp - 1    
