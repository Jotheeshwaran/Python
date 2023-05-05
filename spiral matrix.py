#a=[[1,2,3],[4,5,6],[7,8,9]]
#a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
t=0
n=25
r=c=5
sr=sc=0                                     #Spiral Matrix - Anticlockwise - Method 1
er=ec=r-1
while t<n:
    for i in range(ec,sc-1,-1):
        print(a[sr][i],end=" ")
        t+=1
    sr+=1
    if t==n:
        break
    for j in range(sr,er+1):
        print(a[j][sc],end=" ")
        t+=1
    sc+=1
    if t==n:
        break
    for k in range(sc,ec+1):
        print(a[er][k],end=" ")
        t+=1
    er-=1
    if t==n:
        break
    for l in range(er,sr-1,-1):
        print(a[l][ec],end=" ")
        t+=1
    ec-=1
    if t==n:
        break
    
    
    
    
    
    
    
    
    

#a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
t=0                                             
n=16
r=c=4                                           #Spiral Matrix - Anticlockwise Direction - Method 2
sr=sc=0
er=ec=r-1
a=[]
for i in b:
    i.reverse()
    a.append(i)
while t<n:
    for i in range(sc,ec+1):
        print(a[sr][i],end=" ")
        t+=1
    sr+=1
    if t==n:
        break
    for j in range(sr,er+1):
        print(a[j][ec],end=" ")
        t+=1
    ec-=1
    if t==n:
        break
    for k in range(ec,sc-1,-1):
        print(a[er][k],end=" ")
        t+=1
    er-=1
    if t==n:
        break
    for l in range(er,sr-1,-1):
        print(a[l][sc],end=" ")
        t+=1
    sc+=1
    if t==n:
        break
