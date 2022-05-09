n = int(input())
a = list(map(int ,input().split()))
A = sorted(a)
ans = 0

for i in range(n):
    if A[i] == A[i-1]:
        ans += 1

if ans >= 1:
    print("NO")
elif ans == 0:
    print("YES")