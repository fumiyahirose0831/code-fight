N = int(input())
A = list(input())

box = 1

for i in range(N-1):
    if A[i] != A[i+1]:
        box += 1
print(box)


