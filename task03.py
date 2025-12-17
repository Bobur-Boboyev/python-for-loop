n = int(input("N: "))

if n < 15:
    r = range(n, 15+1)
else:
    r = range(n, 15 - 1, -1)

for i in r:
    print(i)
