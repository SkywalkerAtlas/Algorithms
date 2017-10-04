"""
Author: SkywalkerAtlas
Created at: 3rd Oct, 2017
"""

import inspect


def matrix_chain_order(p):
    """
    Use bottom-up to solve matrix chain multiplication problem, the average time should be O(n^3), and requires O(n^2)
    memory.

    :param p: an array of sizes of matrix
    :return m:
    :return s:
    """

    if type(p) is not list:
        raise TypeError('matrix_chain_order only accept list, not {}'.format(str(type(p))))

    # define a really really big number to represent infinite
    # TODO: I think this could change to something better
    infinite = 2147483647

    n = len(p) - 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]
    s = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        m[i][i] = 0

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j] = infinite
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def find_optimal(s, i, j, result=''):
    """

    :param m: list
    :param s: list
    :param i: start index
    :param j: end index
    """
    if s is None:
        raise TypeError('argument error! s must be list!')
    if i == j:
        result += 'A_{}'.format(i)
    else:
        result += '('
        result += find_optimal(s, i, s[i][j])
        result += find_optimal(s, s[i][j]+1, j)
        result += ')'

    return result


def run_test():
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    print('Need {} ops'.format(m[1][len(p)-1]))
    result = find_optimal(s, 1, len(p)-1, '')
    print('Optimal order is {}'.format(result))



def get_code():
    """
    :return: code for the matrix_chain_multi function
    """
    return inspect.getsource(matrix_chain_order)

