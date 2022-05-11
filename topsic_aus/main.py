N = int(input())
A = list(map(int ,input().split()))
ans = 0
ans1 = 0
#左から
for i in range(N-1):
	ans += max(0,A[i+1] - A[i])
#右から
for x in reversed(range(N-1)):
    ans1 += max(0,A[x] - A[x+1])

print(min(ans1,ans))
