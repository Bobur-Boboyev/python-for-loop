floor = int(input("floor: "))
height = float(input("height: "))

total_height = 0

for i in range(1, floor + 1):
    total_height += height

print(total_height)