import numpy as np
from numpy.testing import assert_almost_equal
from jutil.cg import *


def test_cg():
    import jutil.operator
    n, m = 7, 4
    A = np.random.rand(n, n)
    A = A.T.dot(A)
    for i in range(n):
        A[i, i] += 1  # + i ** 15
    x_tall = np.random.rand(n, m)
    x = x_tall[:, 0]
    b = A.dot(x)
    b_tall = A.dot(x_tall)
    Aj = jutil.operator.JacobiMatrixOperator(A)
    conj_grad_solve(A, b, 100, 0, [1e-20, 1e-4, 1])

    assert_almost_equal(conj_grad_solve(A, b, 100, 0, 1e-20), x)
    assert_almost_equal(conj_grad_tall_solve(A, b_tall, 100, 0, 1e-20), x_tall)
    assert_almost_equal(conj_grad_tall_solve(Aj, b_tall, 100, 0, 1e-20), x_tall)

if __name__ == '__main__':
    from numpy import testing
    testing.run_module_suite()
