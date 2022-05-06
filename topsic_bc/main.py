import collections
S = list(input())

#グループ化して集計
c = collections.Counter(S)

#グループ化した要素の数を集計
print(len(c))