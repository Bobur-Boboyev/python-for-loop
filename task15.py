num = int(input("num: "))

num_str = str(num)
num_reverse = ''

for i in range(len(num_str) - 1, 0 - 1, -1):
    num_reverse += num_str[i]

print(num_reverse)
