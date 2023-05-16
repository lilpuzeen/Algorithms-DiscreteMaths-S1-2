def bracket(n):
    if n == 0:
        return ['']
    else:
        return ['(' + x + ')' + y for i in range(n) for x in bracket(i) for y in bracket(n - i - 1)]


if __name__ == '__main__':
    n = int(input())
    answers = sorted(bracket(n))
    for answer in answers:
        print(answer)