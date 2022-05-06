N = int(input())
d = []
for _ in range(N):
    d.append(int(input()))
ansx = 0
ansX = 0

#X軸グループ（Nの0+偶数）
#足すグループ
for x in range(0,N,4):
    ansx += d[x]
#引くグループ
for X in range(2,N,4):
    ansX += d[X]
X = (ansx-ansX)    



ansy = 0
ansY = 0
#Y軸グループ（Nの奇数）
#引くグループ
for y in range(1,N,4):
    ansy += d[y]
#足すグループ
for Y in range(3,N,4):
    ansY += d[Y]
Y = (ansY - ansy)    

print(X,Y)