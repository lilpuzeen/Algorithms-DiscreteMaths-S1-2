from collections import defaultdict


class Point:
    def __init__(self):
        self.arrows = defaultdict(list)


def add_arrow(states, number: int, arrow: int, c: str):
    states[number].arrows[ord(c) - ord('a')].append(arrow)


def check_string(s: str, current_states: set, states: list, final_states: list) -> bool:
    for i in range(len(s)):
        endpoints = set()
        for j in current_states:
            for arrow in states[j].arrows[ord(s[i]) - ord('a')]:
                endpoints.add(arrow)
        current_states = endpoints
    for i in current_states:
        if final_states[i]:
            return True
    return False


if __name__ == '__main__':
    with open("problem2.in", "r") as f:
        s = f.readline().strip()
        n, m, k = map(int, f.readline().split())
        current_states = {0}
        states = [Point() for _ in range(n)]
        final_states = [False for _ in range(n)]
        for i in map(int, f.readline().split()):
            final_states[i - 1] = True
        for i in range(m):
            line = f.readline().split()
            a, b, c = int(line[0]), int(line[1]), line[2]
            add_arrow(states, a - 1, b - 1, c)

    with open("problem2.out", "w") as fout:
        fout.write("Accepts" if check_string(s, current_states, states, final_states) else "Rejects")
