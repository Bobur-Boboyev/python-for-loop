start = int(input("start: "))
step = int(input("step: "))

if start < 15:
    r = range(start, 15 + 1, +step)
else:
    r = range(start, 15 - 1, -step)

for i in r:
    print(i)
