lst = [int(i) for i in input().split()]
x = int(input())
t = []
for i in range(len(lst)):
    if x == lst[i]:
        t.append(i)
    else:
        continue
if len(t) > 0:
    print(' '.join([str(i) for i in t]))
else:
    print('This number is not found')