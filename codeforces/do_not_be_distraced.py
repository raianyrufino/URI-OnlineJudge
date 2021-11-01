t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())

    done = set()

    previous = ''
    suspicious = 'YES'
    li = 0
    while li < n:
        if s[li] != previous:
            if s[li] in done:
                suspicious = 'NO'
                break
            done.add(s[li])
            previous = s[li]

        li += 1

    print(suspicious)
