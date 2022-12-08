n = int(input("Enter a number for the patter -->  "))
fields = 2*n+1
pattern = [" "for i in range(n)]
count = 0 
temp = n
if n % 2 == 0 :
        count = n / 2
else:         
while temp > 0:
    
    temp = temp - 1
