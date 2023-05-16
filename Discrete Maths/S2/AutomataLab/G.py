from typing import List
from collections import deque

n1, m1, k1, n2, m2, k2 = 0, 0, 0, 0, 0, 0


def add_transition(v: List[List[int]], a: int, b: int, c: str) -> None:
    v[a][ord(c) - ord('a')] = b


def bfs(Q: deque) -> bool:
    temp = (1, 1)
    Q.append(temp)
    while Q:
        curr = Q.popleft()
        if curr[0] != 0:
            visited1[curr[0]] = True
        if curr[1] != 0:
            visited2[curr[1]] = True
        if finalstates1[curr[0]] != finalstates2[curr[1]]:
            return False
        for i in range(26):
            u = aut1[curr[0]][i]
            v = aut2[curr[1]][i]
            if not visited1[u] or not visited2[v]:
                if v != 0 or u != 0:
                    Q.append((u, v))
    return True


def main():
    global n1, m1, k1, n2, m2, k2, aut1, aut2, finalstates1, finalstates2, visited1, visited2
    with open('equivalence.in', 'r') as fin:
        n1, m1, k1 = map(int, fin.readline().split())
        n1 += 1
        finalstates1 = [False] * n1
        aut1 = [[0] * 26 for _ in range(n1)]
        visited1 = [False] * n1
        for x in map(int, fin.readline().split()):
            finalstates1[x] = True
        for _ in range(m1):
            a, b, c = fin.readline().split()
            add_transition(aut1, int(a), int(b), c)

        n2, m2, k2 = map(int, fin.readline().split())
        n2 += 1
        finalstates2 = [False] * n2
        aut2 = [[0] * 26 for _ in range(n2)]
        visited2 = [False] * n2
        for x in map(int, fin.readline().split()):
            finalstates2[x] = True
        for _ in range(m2):
            a, b, c = fin.readline().split()
            add_transition(aut2, int(a), int(b), c)

    Q = deque()
    ans = "YES" if bfs(Q) else "NO"
    with open('equivalence.out', 'w') as fout:
        fout.write(ans)


if __name__ == "__main__":
    main()
