list = [int(i) for i in input().split()]
result = []
if len(list) == 1:
    result.append(list[0])
else:
    result.append(list[1] + list[-1])
    for i in range(1, len(list) - 1):
        result.append(list[i-1] + list[i+1])
    result.append(list[-2] + list[0])
print(' '.join([str(i) for i in result]))