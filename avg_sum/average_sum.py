a = int(input())
b = int(input())
s1 = 0
n1 = 0
s2 = 0
n2 = 0
s = 0
n = 0
if a < 0 and b > 0:
    a = a * (-1)
    for i in range(0, a+1):
        if i % 3 == 0:
            s1 = s1 + i
            n1 += 1
    s1 = s1 * (-1)
    for j in range(1, b+1):
        if  j % 3 == 0:
            s2 = s2 + j
            n2 += 1
    avg = (s1 + s2)/(n1 + n2)
elif a < 0 and b <= 0:
    for l in range (a, b+1):
        if l % 3 == 0:
            s = s + l
            n += 1
    avg = s/n
elif a>=0:
    for k in range(a, b+1):
        if k % 3 == 0:
            s = s + k
            n += 1
    avg = s/n
print(avg)

