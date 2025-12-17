num = int(input("Number of phones: "))

total =  0

for i in range(1, num + 1):
    price = float(input(f"{i}-phone's price: "))
    if price % 5 == 0:
        total += price

print(total)