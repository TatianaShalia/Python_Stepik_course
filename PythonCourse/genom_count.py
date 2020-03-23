s = input()
g = s.upper().count('g'.upper())
c = s.upper().count('c'.upper())
print(((c+g)/len(s))*100)