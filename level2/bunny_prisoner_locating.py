def solution(x, y):
    # Your code here
    # sum of oblique triangle before (x, y)
    sum_last = (1 + (x + y - 2)) * (x + y - 2) // 2
    return str(x + sum_last)


if __name__ == '__main__':
    print(solution(1, 1))
