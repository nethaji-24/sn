s,u=list(map(int,input().split()))
l=[]
for i in range(s+1,u):
  if i%2==0:
    l.append(i)
print(*l)