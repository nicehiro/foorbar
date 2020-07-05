from fractions import Fraction
from copy import deepcopy


def construct_matrix_from_n(a, s_x, e_x, s_y, e_y):
    res = []
    for item in a[s_x:e_x]:
        res.append(item[s_y:e_y])
    return res


def get_matrix_shape(a):
    r = len(a)
    l = len(a[0])
    return r, l


def matrix_sub(m_a, m_b):
    m_a_r, m_a_l = get_matrix_shape(m_a)
    m_b_r, m_b_l = get_matrix_shape(m_b)
    if m_a_r == m_b_r and m_a_l == m_b_l:
        for i in range(m_a_r):
            for j in range(m_a_l):
                m_b[i][j] = m_a[i][j] - m_b[i][j]
        return m_b


def gaussian_elimination(a):
    x, y = len(a), len(a[0])
    for i in range(x):
        if a[i][i] == 0:
            for j in range(i + 1, x):
                if a[j][i] != 0:
                    swap_matrix_rows(a, i, j)
                    break
        if a[i][i] == 0:
            continue
        t = a[i][i]
        for k in range(y):
            a[i][k] /= t
        for k in range(0, x):
            if k != i and a[k][i] != 0:
                t = a[k][i]
                for l in range(i, y):
                    a[k][l] -= a[i][l] * t
    return a


def get_inverse(a):
    l = len(a)
    res = []
    for row in a:
        res.append(row[l:])
    return res


def swap_matrix_rows(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t
    return a


def get_matrix_extense(a):
    l = len(a)
    for i in range(l):
        a[i] += [Fraction(1, 1) if x == i else Fraction(0, 1) for x in range(l)]
    return a


def matrix_mut(m_a, m_b):
    m_a_r, m_a_l = get_matrix_shape(m_a)
    m_b_r, m_b_l = get_matrix_shape(m_b)
    res = [[0 for _ in range(m_b_l)] for _ in range(m_a_r)]
    if m_a_l == m_b_r:
        for i in range(m_a_r):
            for j in range(m_b_l):
                for k in range(m_a_l):
                    res[i][j] += m_a[i][k] * m_b[k][j]
        return res


def gcd(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x % y)

    return gcd1(abs(x), abs(y))


def lcm(x, y):
    return int(x * y / gcd(x, y))


def transform(m):
    mat = deepcopy(m)
    orders = []
    states_n = len(mat[0])
    I_n = 0
    n = {i: [0 for _ in range(states_n)] for i in range(states_n)}
    for i, row in enumerate(mat):
        if sum(row) == 0:
            orders.append(i)
            I_n += 1
    for i, row in enumerate(mat):
        if sum(row) != 0:
            orders.append(i)
        else:
            mat[i][i] = 1
    for i in orders:
        for j in range(states_n):
            n[i][j] = Fraction(mat[i][orders[j]], sum(mat[i]))
    return I_n, states_n, [n[i] for i in orders]


def splitQR(mat, lengthR):
    lengthQ = len(mat) - lengthR
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i == j) - mat[i][j] for j in range(lengthQ)])
        R.append(mat[i][lengthQ:])
    return [Q, R]


def solution(m):
    # Your code here
    I_n, states_n, b = transform(m)
    if I_n == states_n:
        res = [1 for _ in range(I_n)]
        res.append(sum(res))
        return res
    I = [[1 if x == y else 0 for x in range(states_n - I_n)] for y in range(states_n - I_n)]
    R = construct_matrix_from_n(b, I_n, states_n, 0, I_n)
    Q = construct_matrix_from_n(b, I_n, states_n, I_n, states_n)
    Q = matrix_sub(I, Q)

    I_Q = get_matrix_extense(Q)
    I_Q_1 = gaussian_elimination(I_Q)
    I_Q_1 = get_inverse(I_Q_1)
    res = matrix_mut(I_Q_1, R)
    # lcm_res = lcm([x.denominator if x.numerator != 0 else 0 for x in res[0]])
    lcm_res = 1
    for item in res[0]:
        lcm_res = lcm(lcm_res, item.denominator)
    result = [x.numerator * lcm_res // x.denominator for x in res[0]]
    result.append(lcm_res)
    return result


# m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# m = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
m = [[0]]
# m = [
#     [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
#     [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
#     [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
#     [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# m = [
#     [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
#     [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
#     [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
#     [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
#     [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# m = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# m = [
#     [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# m = [
#     [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
#     [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
#     [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
m = [
    [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
    [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
    [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
    [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print(solution(m))
