n = int(input("N: "))

if n < 1:
    r = range(1, n - 1, -1)
else:
    r = range(1, n+1)

for i in r:
    print(i)