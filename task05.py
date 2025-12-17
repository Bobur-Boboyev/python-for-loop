start = int(input("start: "))
end = int(input("end: "))

if start < end:
    r = range(start, end + 1)
else:
    r = range(start, end-1, -1)

for i in r:
    print(i)