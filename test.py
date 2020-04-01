from tools import linalg as la
import numpy as np

if __name__ == "__main__":
    R = np.arange(9).reshape(3, 3)
    print(R)

    t = np.arange(3)

    print(t)

    T = np.array([
        [0, 1, 2, 0],
        [3, 4, 5, 1],
        [6, 7, 8, 2],
        [0, 0, 0, 1]
    ])

    T_est = la.Rt2T(R, t)
    print(T_est)

    assert(T.all()==T_est.all())