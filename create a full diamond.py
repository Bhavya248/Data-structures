# full diamond pattern
n = int(input("Enter a number for the pattern -->  "))
fields = 2*n+1
pattern = [" "for i in range(fields)]
pattern_list = [pattern for i in range(n)]
count = 0 
temp = n
if n % 2 == 0 :
        count = int(n / 2)
else: 
    count = int((n + 1) / 2)
inex_a = int((fields+1)/2)
inex_b = int((fields+1)/2)
print(pattern_list)            
for i in range(n):
    pattern_list[i][inex_a-1]="*"
    pattern_list[i][inex_b-1]="*"
    print(pattern_list[i])
    print(" ".join(pattern_list[i]))
    inex_a = inex_a + 1
    inex_b = inex_b - 1
print(pattern_list)   

