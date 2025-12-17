total_age = 0

for i in range(1, 6):
    age = int(input(f"{i}-student's age: "))
    total_age += age

average = total_age / 5

print(average)