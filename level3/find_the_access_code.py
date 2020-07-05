res = 0


def solution(l):
    # Your code here
    n = len(l)
    res = [1 for _ in range(n)]
    relations = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                relations[i].append(j)
    for k in range(2):
        for i in range(n):
            t = 0
            for j in relations[i]:
                t += res[j]
            res[i] = t
    return sum(res)


def can_divided(x, y):
    # check if x can divid y
    return x % y == 0


def recursive(start_pos, prev, left, l):
    if left == 0:
        global res
        res += 1
        return
    if start_pos >= len(l):
        return
    if can_divided(l[start_pos], prev):
        recursive(start_pos + 1, l[start_pos], left - 1, l)
    recursive(start_pos + 1, prev, left, l)


if __name__ == '__main__':
    # l = [1, 1, 1]
    # l = [1, 2, 3, 4, 5, 6, 7]
    # l = [1, 5, 6]
    l = range(1, 2001)
    print(solution(l))
