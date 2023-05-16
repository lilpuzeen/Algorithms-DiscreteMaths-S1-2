def accepts_DFA(word, endpoints, arrows):
    current_state = 1
    for char in word:
        found_arrow = False
        for arrow in arrows:
            if arrow[0] == current_state and arrow[2] == char:
                current_state = arrow[1]
                found_arrow = True
                break
        if not found_arrow:
            return "Rejects"
    if current_state in endpoints:
        return "Accepts"
    else:
        return "Rejects"


if __name__ == '__main__':
    fin = open("problem1.in", "r")
    fout = open("problem1.out", "w")
    word = fin.readline().strip()
    n, m, k = map(int, fin.readline().split())
    endpoints = [int(item) for item in fin.readline().split()]
    arrows = []
    for i in range(m):
        line = fin.readline().split()
        arrows.append((int(line[0]), int(line[1]), line[2]))

    fout.write(accepts_DFA(word, endpoints, arrows))