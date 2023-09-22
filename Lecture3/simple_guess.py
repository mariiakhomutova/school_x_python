def guess(N: int) -> int | str:
    for i in range(1, N+1):
        if N / i == i:
            return i
    return 'трудно, не могу'

y = int(input())
answer = guess (y)
print(answer)