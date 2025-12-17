max_score = 0
min_score = 0

for i in range(1, 6):
    score = int(input(f"{i}-student's score: "))
    if i == 1:
        max_score = score
        min_score = score
    else:
        if max_score < score:
            max_score = score
        if min_score > score:
            min_score = score

print(f"Eng yuqori: {max_score}, Eng past: {min_score}")