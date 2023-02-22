n = int(input())
l = []
s = []
for i in range(n):
    a = input().lower()
    x = l.append(a)

for j in l:
    if (j in s)==False:
        w = s.append(j)
print(len(s))

for k in range(len(s)):
    c = l.count(s[k])
    print(c,end = ' ')
