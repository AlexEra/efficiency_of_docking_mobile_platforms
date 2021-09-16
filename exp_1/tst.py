import numpy as np


if __name__ == '__main__':
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    # print('{}\n {}\n {}'.format(x.shape(), y.shape(), z.shape()))
