def reverse(n):
    i = 0
    while n > 0:
        mod = n % 10
        n = n // 10
        i = i * 10 + mod
    return (i)
