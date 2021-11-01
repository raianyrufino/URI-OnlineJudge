def check_password_in_hash_slice(password, hash):
    p = list(password)
    for c in hash:
        if c in p:
            p.pop(p.index(c))
        else: return False
    return True


t = int(input())

for _ in range(t):
    p = input()
    h = input()

    diff = len(h) - len(p)
    i = 0
    password_in_hash = False
    while i <= diff:
        password_in_hash = check_password_in_hash_slice(p, h[i:i+len(p)])
        if password_in_hash: break
        i += 1

    print('YES' if password_in_hash else 'NO')

