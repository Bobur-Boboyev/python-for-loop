num = int(input("Products number: "))

total_price = 0

for i in range(1, num + 1):
    price = float(input(f"{i}-product's price: "))
    discount = price * 0.10
    discounted_price = price - discount
    total_price += discounted_price

print(total_price)