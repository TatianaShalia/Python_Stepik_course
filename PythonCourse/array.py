row = ''
array = []
while True:
    row = input()
    if row == 'end':
        break
    array.append([int(k) for k in row.split()])
m = len(array)
n = len(array[0])
sum_array = [[sum([array[i - 1][j], array[(i - m + 1)][j], array[i][j - 1], array[i][(j - n + 1)]]) for j in range(n)]
             for i in range(m)]
for i in range(m):
    for j in range(n):
        print(sum_array[i][j], end=' ')
    print()
