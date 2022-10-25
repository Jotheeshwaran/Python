r2=int(input())
c2=int(input())
r1=0
c1=0
e=[]
h=[]
for i in range(r2):
    t=[]
    for j in range(c2):
        x=int(input())
        t.append(x)
    e.append(t)
while r1<r2 and c1<c2:
    for i in range(c1,c2):
        h.append(e[r1][i])
    r1=r1+1
    for j in range(r1,r2):
        h.append(e[j][c2-1])
    c2=c2-1
    x=c2-1
    if r1<r2:
        while x>=c1:
            h.append(e[r2-1][x])
            x=x-1
    r2=r2-1
    y=r2-1
    if c1<c2:
        while y>=r1:
            h.append(e[y][c1])
            y=y-1
    c1=c1+1
print(h)
