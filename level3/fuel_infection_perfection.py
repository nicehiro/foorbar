def solution(n):
    # Your code here
    # Failed with one testcase.
    # If someone know the answer please tell me. Thanks!
    min_steps = {1: 0, 2: 1}

    def recursive(i):
        if i in min_steps:
            return min_steps.get(i)
        for j in range(1027, 0, -1):
            if i % (2 ** j) == 0:
                min_steps[i] = recursive(i // 2 ** j) + j
                return min_steps[i]
        min_steps[i] = min(recursive((i + 1) // 2) + 2,
                           recursive((i - 1) // 2) + 2)
        return min_steps[i]

    n = int(n)
    recursive(n)
    return min_steps[n]


def solution2(n):
    # Failed with google special settings
    # BLACKED_LIST_CODE
    import sys
    sys.setrecursionlimit(int(1e9))
    min_steps = {1: 0, 2: 1}

    def recursive(i):
        if i in min_steps:
            return min_steps.get(i)
        if i % 2 == 0:
            min_steps[i] = recursive(i // 2) + 1
        else:
            min_steps[i] = min(recursive((i + 1) // 2) + 1,
                               recursive((i - 1) // 2) + 1)
        return min_steps[i]

    n = int(n)
    recursive(n)
    return min_steps[n]


def solution3(n):
    # Passed!
    n = int(n)
    res = 0
    while (n != 1):
        if (n % 2 == 0):
            n = n / 2
        elif ((n == 3) or ((n + 1) & n) > ((n - 1) & (n - 2))):
            n -= 1
        else:
            n += 1
        res += 1
    return res


def solution4(n):
    # Passed!
    # based on solution:
    # https://stackoverflow.com/questions/45790229/google-foobar-how-to-find-edge-cases-and-identify-test-cases-python
    n = int(n)
    res = 0
    while n != 1:
        if n & 1 == 0:
            n = n >> 1
            res += 1
        else:
            a = n + 1
            b = n - 1
            ac = bc = 0
            while a & 1 == 0:
                a = a >> 1
                ac += 1
            while b & 1 == 0:
                b = b >> 1
                bc += 1
            if ac > bc and n != 3:
                n = a
                res += ac + 1
            else:
                n = b
                res += bc + 1
    return res


if __name__ == '__main__':
    n = '9' * 309
    # n = str(2 ** 1024)
    # n = '3'
    print(solution4(n))
