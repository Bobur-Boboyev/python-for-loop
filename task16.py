min_num = 0

for i in range(1, 7 + 1):
    num = int(input(f"{i}-num: "))
    if i == 1:
        min_num = num
    elif min_num > num:
        min_num = num
    
print(min_num)
