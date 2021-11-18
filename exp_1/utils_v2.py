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


def eta_l(l_r, p_r):
    return 0.14980 + 0.04462 * l_r + 3.14000 * p_r - 2.14700 * l_r ** 2 + 0.36250 * l_r * p_r - \
                             3.56600 * p_r ** 2 + 3.98200 * l_r ** 3 - 0.02121 * l_r ** 2 * p_r - 0.54390 * l_r * \
                             p_r ** 2 + 1.15000 * p_r ** 3


def eta_h(h_r, p_r):
    return 0.24020 - 0.19360 * h_r + 2.32200 * p_r - 0.48210 * h_r ** 2 + 0.10420 * h_r * \
           p_r - 1.77400 * p_r ** 2


def calculate_efficiency(x, y, z, params, b_ang, g_ang):
    platform_len, d, p_rel, n_max, l_m = params
    n_rel_h, n_rel_l, n_rel = list(), list(), list()
    l_lst, h_lst = list(), list()
    n_a, n_b = list(), list()
    for c_0, c_1, l_n, bet, gam in zip(x, y, z, b_ang, g_ang):
        l_n -= platform_len
        l_rel = l_n / d
        l_lst.append(l_n)
        n_rel_l.append(eta_l(l_rel, p_rel))

        n_a.append(eta_l((l_n - d/2 * math.sin(gam * math.pi / 180)) / d, p_rel) *
                   eta_l((l_n + d/2 * math.sin(gam * math.pi / 180)) / d, p_rel))
        n_b.append(eta_l((l_n - d/2 * math.sin(bet * math.pi / 180)) / d, p_rel) *
                   eta_l((l_n - d/2 * math.sin(bet * math.pi / 180)) / d, p_rel))

        g = (c_0 ** 2 + c_1 ** 2) ** (1 / 2)
        h_rel = g / d
        h_lst.append(g)
        n_rel_h.append(eta_h(h_rel, p_rel))

    for c_n in range(len(n_rel_h)):
        n_rel.append(round(n_rel_h[c_n] * (n_a[c_n] + n_b[c_n] + n_rel_l[c_n]) / 3 * n_max, 3))
    return n_rel, l_lst, h_lst


def time_charging(eff_lst, p_1_max, c_t=60):
    t = list()
    for e in eff_lst:
        t.append(c_t / (p_1_max * e))
    return t


def graph_3d(x, y, z, x_label, y_label):
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 14
    j = 0
    for i in z:
        z[j] = i * 100
        j += 1
    x = np.array(x)
    y = np.array(y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, s=80)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(r'$\eta_s$')
    plt.show()


def graph_2d(x, y, x_label, y_label, is_y_eff):
    if is_y_eff:
        for i in range(len(y)):
            y[i] = round(y[i] * 100, 2)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 14
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


def graph_gisto(x, y, x_label, y_label):
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 14
    ax = plt.subplot()
    ax.bar(range(len(x)), y, 0.35, color="w", edgecolor="k")
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x)
    ax.grid()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def get_std(avg_values, values):
    tmp = [0 for i in range(14)]
    for i in range(len(avg_values)):
        for j in range(len(values[i])):
            tmp[i] += (avg_values[i] - values[i][j] * 100) ** 2
        tmp[i] = (tmp[i]) ** (1 / 2) / 8.485
    return tmp


def d_interval(avg_vls, std_vls):
    res = list()
    for i in range(len(avg_vls)):
        res.append([avg_vls[i] - 1.83311 * std_vls[i] / 3, avg_vls[i] + 1.83311 * std_vls[i] / 3])
    return res


def graph_gisto_fig7(x, y, all_y, x_label, y_label):
    # y - list of means
    y_std = get_std(y, all_y)
    intervals = d_interval(y, y_std)
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 14
    ax = plt.subplot()
    ax.bar(range(len(x)), y, 0.35, color="w", edgecolor="k")
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x)
    ax.grid()
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    for i_s in range(14):
        ax.plot([i_s, i_s], intervals[i_s], 'k')

    plt.show()
    return intervals
