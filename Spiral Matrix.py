a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
e=[]
r1=0
r2=b[0]
c1=0
c2=b[1]
r=[[0 for i in range(c2)] for j in range(r2)]
k=0
h=[]
m=b[-1]
for i in range(r2):
    d=[]
    for j in range(c2):
        f=c[k]
        d.append(f)
        k=k+1
    e.append(d)
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
print(h[m-1])