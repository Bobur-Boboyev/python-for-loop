n = int(input("N: "))

max_num = 0
min_num = 0

for i in range(1, n + 1):
    num = int(input(f"{i}-num: "))
    if i == 1:
        max_num = num
        min_num = num
    else:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num

average = (min_num + max_num) / 2

print(average)
