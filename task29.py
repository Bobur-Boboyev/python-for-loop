n = int(input("Number of outlets: "))

total = 0

for i in range(1, n + 1):
    income = float(input(f"{i}-outlet's income: "))
    total += income

average = total / n

print(average)