import collections
N = int(input())
A = list(map(int ,input().split()))
C = collections.Counter(A)


#グループ集計を左から降順に行い、一番左に数字が１以上（複数あるか）でYESかNOを定義
if C.most_common()[0][0] > 1:
	print("NO")
elif C.most_common()[0][0] <= 1:
    print("YES")