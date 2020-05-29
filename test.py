from tools import linalg as la
import numpy as np

from skylynx.utils import cli_args

if __name__ == "__main__":
    cli_params = dict(task=0,
                      length=10
                      )

    args = cli_args(cli_params)
    task = args['task']

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

    assert(T.all() == T_est.all())
