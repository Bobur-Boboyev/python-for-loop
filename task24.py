total_score = 0

for i in range(1, 11):
    score = int(input(f"{i}-student's score: "))
    total_score += score

print(total_score)