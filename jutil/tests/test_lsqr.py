import numpy as np
from numpy.testing import assert_almost_equal
from jutil.cg import *
from jutil.lsqr import *


def test_lsqr():
    import jutil.operator
    n, m = 7, 4
    A = np.random.rand(n, m)
    ATA = A.T.dot(A)
    b = np.random.rand(7)
    x = conj_grad_solve(ATA, A.T.dot(b), 100, 1e-20, 1e-20)
    x2 = lsqr_solve(A, b, 100, 1e-20, 1e-20, 0)
    assert_almost_equal(x, x2)

if __name__ == '__main__':
    from numpy import testing
    testing.run_module_suite()
