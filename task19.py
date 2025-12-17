n = int(input("N: "))

max_num = 0

for i in range(1, n + 1):
    num = int(input(f"{i}-num: "))
    if i == 1:
        max_num = num
    elif max_num < num:
        max_num = num

print(max_num)