size = int(input())

matrix = []
for row in range(size):
    matrix.append(input().split())

alice_first_row = None
alice_first_col = None
rabbit_row = None
rabbit_col = None
directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}
for i in range(size):
    for j in range(size):
        current_position = matrix[i][j]
        if current_position == 'A':
            alice_first_row = i
            alice_first_col = j
        if current_position == 'R':
            rabbit_row = i
            rabbit_col = j

sum_tea_bags = 0

while sum_tea_bags < 10:
    commands = input()
    ro, co = directions[commands](alice_first_row, alice_first_col)
    matrix[alice_first_row][alice_first_col] = '*'
    if 0 > ro or ro >= size or 0 > co or co >= size:
        break
    if matrix[ro][co] == 'R':
        matrix[ro][co] = '*'
        break

    matrix[alice_first_row][alice_first_col] = '*'

    if matrix[ro][co].isdigit():
        sum_tea_bags += int(matrix[ro][co])
    matrix[ro][co] = '*'
    alice_first_row = ro
    alice_first_col = co

if sum_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')
