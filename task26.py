c = 0

for i in range(1, 8):
    age = int(input(f"{i}-student's age: "))
    if age < 21:
        c += 1

print(c)