n = int(input("N: "))
total = 0

for i in range(1, n + 1):
    total += pow(i, 3)

print(total)