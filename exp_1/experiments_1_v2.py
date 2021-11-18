from utils_v2 import *

"""
TODO:
+ график трехмерный, где будет отображено осевое, радиальное смещение и КПД
+ 2D (гистограмма) график зависимости времени заряда от КПД

Addon:
+- графики зависимости КПД от угла наклона для всех экспериментов
+- время заряда в зависимости от угла наклона
"""

if __name__ == '__main__':
    platform_len = 0.518  # from datasheet, platform length is 0.508 m
    d = 0.08
    p_max = 20
    p_n = 15
    p_rel = p_n / p_max
    n_max = 0.8
    l_m = 0.2
    parameters = [platform_len, d, p_rel, n_max, l_m]

    x_0, y_0, z_0 = catch_a_data('point_1_poses.txt')
    b_0, g_0 = angles_lists(catch_a_data('point_1_orient.txt'))
    n_0, l_0, h_0 = calculate_efficiency(x_0, y_0, z_0, parameters, b_0, g_0)

    x_1, y_1, z_1 = catch_a_data('point_2_poses.txt')
    b_1, g_1 = angles_lists(catch_a_data('point_2_orient.txt'))
    n_1, l_1, h_1 = calculate_efficiency(x_1, y_1, z_1, parameters, b_1, g_1)

    x_2, y_2, z_2 = catch_a_data('point_3_poses.txt')
    b_2, g_2 = angles_lists(catch_a_data('point_3_orient.txt'))
    n_2, l_2, h_2 = calculate_efficiency(x_2, y_2, z_2, parameters, b_2, g_2)

    x_3, y_3, z_3 = catch_a_data('point_4_poses.txt')
    b_3, g_3 = angles_lists(catch_a_data('point_4_orient.txt'))
    n_3, l_3, h_3 = calculate_efficiency(x_3, y_3, z_3, parameters, b_3, g_3)

    x_4, y_4, z_4 = catch_a_data('point_5_poses.txt')
    b_4, g_4 = angles_lists(catch_a_data('point_5_orient.txt'))
    n_4, l_4, h_4 = calculate_efficiency(x_4, y_4, z_4, parameters, b_4, g_4)

    x_5, y_5, z_5 = catch_a_data('point_6_poses.txt')
    b_5, g_5 = angles_lists(catch_a_data('point_6_orient.txt'))
    n_5, l_5, h_5 = calculate_efficiency(x_5, y_5, z_5, parameters, b_5, g_5)

    x_6, y_6, z_6 = catch_a_data('point_7_poses.txt')
    b_6, g_6 = angles_lists(catch_a_data('point_7_orient.txt'))
    n_6, l_6, h_6 = calculate_efficiency(x_6, y_6, z_6, parameters, b_6, g_6)

    x_7, y_7, z_7 = catch_a_data('point_8_poses.txt')
    b_7, g_7 = angles_lists(catch_a_data('point_8_orient.txt'))
    n_7, l_7, h_7 = calculate_efficiency(x_7, y_7, z_7, parameters, b_7, g_7)

    x_8, y_8, z_8 = catch_a_data('point_9_poses.txt')
    b_8, g_8 = angles_lists(catch_a_data('point_9_orient.txt'))
    n_8, l_8, h_8 = calculate_efficiency(x_8, y_8, z_8, parameters, b_8, g_8)

    x_9, y_9, z_9 = catch_a_data('point_10_poses.txt')
    b_9, g_9 = angles_lists(catch_a_data('point_10_orient.txt'))
    n_9, l_9, h_9 = calculate_efficiency(x_9, y_9, z_9, parameters, b_9, g_9)

    x_10, y_10, z_10 = catch_a_data('point_11_poses.txt')
    b_10, g_10 = angles_lists(catch_a_data('point_11_orient.txt'))
    n_10, l_10, h_10 = calculate_efficiency(x_10, y_10, z_10, parameters, b_10, g_10)

    x_11, y_11, z_11 = catch_a_data('point_12_poses.txt')
    b_11, g_11 = angles_lists(catch_a_data('point_12_orient.txt'))
    n_11, l_11, h_11 = calculate_efficiency(x_11, y_11, z_11, parameters, b_11, g_11)

    x_12, y_12, z_12 = catch_a_data('point_13_poses.txt')
    b_12, g_12 = angles_lists(catch_a_data('point_13_orient.txt'))
    n_12, l_12, h_12 = calculate_efficiency(x_12, y_12, z_12, parameters, b_12, g_12)

    x_13, y_13, z_13 = catch_a_data('point_14_poses.txt')
    b_13, g_13 = angles_lists(catch_a_data('point_14_orient.txt'))
    n_13, l_13, h_13 = calculate_efficiency(x_13, y_13, z_13, parameters, b_13, g_13)

    x = l_0 + l_1 + l_2 + l_3 + l_4 + l_5 + l_6 + l_7 + l_8 + l_9 + l_10 + l_11 + l_12 + l_13
    y = h_0 + h_1 + h_2 + h_3 + h_4 + h_5 + h_6 + h_7 + h_8 + h_9 + h_10 + h_11 + h_12 + h_13
    z = n_0 + n_1 + n_2 + n_3 + n_4 + n_5 + n_6 + n_7 + n_8 + n_9 + n_10 + n_11 + n_12 + n_13

    # graph_3d(x, y, z, 'L, м', 'H, м')

    """"""
    t_avg = avg(time_charging(z, p_max))
    b_avg = avg(b_0 + b_1 + b_2 + b_3 + b_4 + b_5 + b_6 + b_7 + b_8 + b_9 + b_10 + b_11 + b_12 + b_13)
    g_avg = avg(g_0 + g_1 + g_2 + g_3 + g_4 + g_5 + g_6 + g_7 + g_8 + g_9 + g_10 + g_11 + g_12 + g_13)
    ar_angle_avg = [6.59, 10.01, 12.05, 18.77, 14.88, 14.53, 17.08, 0, 1.12, 6.83, 12.65, 17.42, 19.33, 19.99]
    n_avg = avg(z)
    for i in range(len(b_avg)):
        b_avg[i] = round(b_avg[i], 2)
        g_avg[i] = round(g_avg[i], 2)
        n_avg[i] = round(n_avg[i] * 100, 2)
    b_g_lst = list()
    for i, j in zip(b_avg, g_avg):
        b_g_lst.append([i, j])
    # n_all = [n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10, n_11, n_12, n_13]
    # res = graph_gisto_fig7(b_g_lst, n_avg, n_all, r'[$\beta, \gamma$], град', 'Эффективность, %')  # fig. 7
    graph_gisto(n_avg, t_avg, 'Эффективность, %', 'Время зарядки, ч')

    """
    tmp = list()
    n_avg = avg(z)
    for i in n_avg:
        tmp.append(round(100 * (n_max - i), 2))
    # print('deviations from maximum efficiency, %: {}'.format(tmp))
    # print('average deviation from maximum efficiency, %: {}'.format(round(sum(tmp) / len(tmp), 2)))
    print(max(n_avg))
    print(min(n_avg))
    """
    """
    l_avg = avg(x)
    h_avg = avg(y)
    for i in range(len(l_avg)):
        l_avg[i] = round(l_avg[i], 4)
        print(l_avg[i])
    print('\n')
    for i in range(len(l_avg)):
        h_avg[i] = round(h_avg[i], 4)
        print(h_avg[i])
    """
