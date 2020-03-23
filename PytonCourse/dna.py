s = input()
n = 1
i = 0
result = ''
while i < (len(s) - 1):
    if s[i] == s[i+1]:
        n += 1
    else:
        result += s[i] + str(n)
        n = 1
    i += 1
print(result + s[i] + str(n))