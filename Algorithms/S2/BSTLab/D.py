n, m = map(int, input().split())
a = [0] * (m+1)
max_pos = 0


def insert_key(l, k):
    global max_pos
    if l > m:
        return
    if a[l] == 0:
        a[l] = k
        max_pos = max(max_pos, l)
    else:
        insert_key(l+1, a[l])
        insert_key(l, k)


for i in range(n):
    l, k = map(int, input().split())
    insert_key(l, k)

print(max_pos)
for i in range(1, max_pos+1):
    print(a[i], end=' ')
