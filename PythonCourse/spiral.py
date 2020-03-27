n = int(input())
di = 1
dj = 0
i = 0
j = 0
array = [[0] * n for k in range(n)]
for a in range(1, n**2+1):
    array[i][j] = a
    ci = i + di
    cj = j + dj
    if 0 <= ci < n and 0 <= cj < n and not array[ci][cj]:
        i = ci
        j = cj
    else:
        di, dj = -dj, di
        i, j = i + di, j + dj
for j in range(n):
    for i in range(n):
        print(array[i][j], end=' ')
    print()
