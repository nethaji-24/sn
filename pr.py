def check(q,l):
    t=l[0]
    m = []
    for i in range(len(q)):
        for j in range(1,len(l)):
            y=l[j]
            if j==(len(l)-1) and t[i] == y[i]:
                m.append(t[i])
            elif t[i] == y[i]:
                continue
            else:
                return m
    return m
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
q=min(l)
print("".join(check(q,l)))
