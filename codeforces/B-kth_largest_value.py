n, q = map(int, input().split())
a = list(map(int, input().split()))

c = a.count(1)

for i in range(q):
    t, num = map(int, input().split())

    if t == 1:
        a[num-1] = 1 - a[num-1]
        c += -1 if a[num-1] == 0 else 1
    else:
        print(1 if num <= c else 0)
