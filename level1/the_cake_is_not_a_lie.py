def solution(s):
    # Your code here
    l = len(s)
    for i in range(1, l // 2 + 1):
        if l % i != 0:
            continue
        j = 0
        temp = s[:i]
        while j < l:
            if s[j:j + i] != temp:
                break
            j += i
        if j >= l:
            return l // i
    return 1


if __name__ == '__main__':
    s = 'abc'
    print(solution(s))
