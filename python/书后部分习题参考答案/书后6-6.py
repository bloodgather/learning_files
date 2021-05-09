def series(index):
    if index > 3:
        return series(index - 1) + series(index - 2) + series(index - 3)
    else:
        return 1

ans = []
for i in range(1,21):
    ans.append(series(i))
print(ans)
