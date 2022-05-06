n = int(input())

ans = 0

#ちょうどでないとき
if n % 100 != 0:
    ans = -1
else:
    ans += n // 500
    n %= 500
    #print('500円：',ans,'枚',sep='')
    ans += n // 100
    n %= 100
    #print('100円：',ans,'枚',sep='')

print(ans)