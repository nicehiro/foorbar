def solution(h, q):
    # Your code here
    max_n = 2 ** h - 1

    def find_x(low, high, x):
        father = high
        left_high = (high - low) // 2 + low - 1
        right_low = left_high + 1
        right_high = high - 1
        if x == left_high or x == right_high:
            return father
        if x < left_high:
            return find_x(low, left_high, x)
        if x < right_high:
            return find_x(right_low, right_high, x)

    res = []
    for x in q:
        if x >= max_n or x <= 0:
            res.append(-1)
        else:
            res.append(find_x(1, max_n, x))
    return res


if __name__ == '__main__':
    print(solution(3, [7, 3, 5, 1]))
