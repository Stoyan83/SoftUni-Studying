size = 6

matrix = []

score = 0

for rows in range(size):
    matrix.append([int(x) if x.isdigit() else x for x in input().split()])

for _ in range(3):
    current_shot = input().replace('(', "").replace(')', "")
    current_row, current_col = [int(x) for x in current_shot.split(", ")]
    if 0 <= current_row < size and 0 <= current_col < size:
        if matrix[current_row][current_col] == "B":
            for row in range(6):
                for col in range(current_col, current_col + 1):
                   if isinstance(matrix[row][col],int):
                       score += matrix[row][col]
            matrix[current_row][current_col] = 0



if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
if score in range(100, 200):
    print(f"Good job! You scored {score} points, and you've won Football.")
elif score in range(200,300):
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
elif score > 299:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")