n = int(input('N: '))

juft_yigindi = 0
toq_yigindi = 0

for i in range(n + 1):
    if i % 2 == 0:
        juft_yigindi += i
    else:
        toq_yigindi += i

print(f"Juft: {juft_yigindi}")
print(f"Toq: {toq_yigindi}")