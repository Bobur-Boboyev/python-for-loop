max_price = 0
min_price = 0

for i in range(1, 6):
    price = int(input(f"{i}-phone's price: "))
    if i == 1:
        max_price = price
        min_price = price
    else:
        if max_price < price:
            max_price = price
        if min_price > price:
            min_price = price

average = (min_price + max_price) / 2

print(average)