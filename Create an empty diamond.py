n = int(input('Enter the floor for pattern --> '))
horizontal_length = 2*n - 1
vertical_length = 2*n - 1
pattern = [" " for i in range(vertical_length)]
index_a = int((horizontal_length - 1)/2)
index_b = int((horizontal_length - 1)/2)
while (index_a > 0 and index_b < horizontal_length):
    pattern[index_a] = "*"
    pattern[index_b] = "*"
    index_a -= 1
    index_b += 1
    print(" ".join(pattern))
    pattern = [" " for i in range(vertical_length)]

while (index_a <= index_b and index_b >= index_a):
    pattern[index_a] = "*"
    pattern[index_b] = "*"
    index_a += 1
    index_b -= 1
    print(" ".join(pattern))
    pattern = [" " for i in range(vertical_length)]
