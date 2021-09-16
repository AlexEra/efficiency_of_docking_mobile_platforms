import numpy as np
import math
import cv2
import matplotlib.pyplot as plt


def rotmtx_to_euler_angles(r):
    sy = math.sqrt(r[0, 0] * r[0, 0] + r[1, 0] * r[1, 0])
    singular = sy < 1e-6
    if not singular:
        a = math.atan2(r[2, 1], r[2, 2])
        b = math.atan2(-r[2, 0], sy)
        c = math.atan2(r[1, 0], r[0, 0])
    else:
        a = math.atan2(-r[1, 2], r[1, 1])
        b = math.atan2(-r[2, 0], sy)
        c = 0
    return np.array([a, b, c])


def angles_lists(t):
    beta_lst, gamma_lst = list(), list()
    x, y, z = t
    for r_0, r_1, r_2 in zip(x, y, z):
        _, beta, gamma = rotmtx_to_euler_angles(cv2.Rodrigues(np.array([r_0, r_1, r_2]).reshape(3, 1))[0])
        beta_lst.append(beta * 180 / math.pi)
        gamma_lst.append(gamma * 180 / math.pi)
    return beta_lst, gamma_lst


def catch_a_data(file):
    a, b, c = list(), list(), list()
    with open(file, 'r') as f:
        data = f.read().split('\n')
        for line in data:
            line = line.split(' ')
            a.append(float(line[0]))
            b.append(float(line[1]))
            c.append(float(line[2]))
    return a, b, c


def calculate_efficiency(x, y, z, params):
    platform_len, d, p_rel, n_max = params
    n_rel_h, n_rel_l, n_rel = list(), list(), list()
    l_lst, h_lst = list(), list()
    for c_0, c_1, l_n in zip(x, y, z):
        l_n -= platform_len
        l_rel = l_n / d
        l_lst.append(l_n)
        n_rel_l.append(round(0.14980 + 0.04462 * l_rel + 3.14000 * p_rel - 2.14700 * l_rel ** 2 + 0.36250 * l_rel
                             * p_rel - 3.56600 * p_rel ** 2 + 3.98200 * l_rel ** 3 - 0.02121 * l_rel ** 2 * p_rel -
                             0.54390 * l_rel * p_rel ** 2 + 1.15000 * p_rel ** 3, 3))

        g = (c_0 ** 2 + c_1 ** 2) ** (1 / 2)
        h_rel = g / d
        h_lst.append(g)
        n_rel_h.append(round(0.24020 - 0.19360 * h_rel + 2.32200 * p_rel - 0.48210 * h_rel ** 2 + 0.10420 * h_rel *
                             p_rel - 1.77400 * p_rel ** 2, 3))

    for n_0, n_1 in zip(n_rel_h, n_rel_l):
        n_rel.append(round(n_0 * n_1 * n_max, 3))
    return n_rel, l_lst, h_lst


def time_charging(eff_lst, p_1_max, c_t=60):
    t = list()
    for e in eff_lst:
        t.append(c_t / (p_1_max * e))
    return t


def graph_3d(x, y, z, x_label, y_label):
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    j = 0
    for i in z:
        z[j] = i * 100
        j += 1
    x = np.array(x)
    y = np.array(y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=80)
    # ax.plot(x, y, z, label='parametric curve')
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(r'$\eta_s$')
    plt.show()


def graph_2d(x, y, x_label, y_label, is_y_eff):
    if is_y_eff:
        for i in range(len(y)):
            y[i] = round(y[i] * 100, 2)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    plt.plot(x, y)
    # plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def avg(src_lst):
    lst_avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    left = 0
    right = 10
    count = 0
    for i in range(len(src_lst)):
        if left <= i < right:
            lst_avg[count] += src_lst[i]
            if i == right - 1:
                lst_avg[count] /= right - left
                count += 1
                left += 10
                right += 10
    return lst_avg


def graph_gisto(t_s, n):
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 12
    t_avg = avg(t_s)
    n_avg = avg(n)
    for i in range(len(n_avg)):
        n_avg[i] = round(n_avg[i] * 100, 2)
    ax = plt.subplot()
    ax.bar(range(14), t_avg, 0.35)
    ax.set_xticks(range(14))
    ax.set_xticklabels(n_avg)
    ax.grid()
    ax.set_ylabel('Время зарядки, ч')
    ax.set_xlabel('КПД, %')
    plt.show()
