A = input()
B = input()

if A.upper() == B.upper():
	ans = "YES"
elif A.lower() == B.lower():
	ans = "YES"
else:
	ans = "NO"

print(ans)