import numpy as np


def Rt2T(R, t):
    """Construct 4x4 Transformation matrix

    Arguments:
        R {[type]} -- [description]
        t {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    T = np.identity(4)
    T[:3, :3] = R
    T[:3, 3] = t
    return T


def T2Rt(T):
    R = T[:3, :3]
    t = T[:3, 3]
    return R, t


if __name__ == "__main__":
    pass
