def catch_a_data(file):
    a, b, c = list(), list(), list()
    with open(file, 'r') as f:
        data = f.read().split(',\n')
        for line in data:
            line = line.split(',')
            a.append(float(line[0]))
            b.append(float(line[1]))
            c.append(float(line[2]))
    return a, b, c


def calculate_efficiency(x, y, z):
    n_rel_h, n_rel_l, n_rel = list(), list(), list()
    for c_0, c_1, l_n in zip(x, y, z):
        l_n -= platform_len
        # print(round(l_n, 4))
        l_rel = l_n / d
        n_rel_l.append(round(0.14980 + 0.04462 * l_rel + 3.14000 * p_rel - 2.14700 * l_rel ** 2 + 0.36250 * l_rel
                             * p_rel - 3.56600 * p_rel ** 2 + 3.98200 * l_rel ** 3 - 0.02121 * l_rel ** 2 * p_rel -
                             0.54390 * l_rel * p_rel ** 2 + 1.15000 * p_rel ** 3, 3))

        g = (c_0 ** 2 + c_1 ** 2) ** (1 / 2)
        # print(round(g, 3))
        h_rel = g / d
        n_rel_h.append(round(0.24020 - 0.19360 * h_rel + 2.32200 * p_rel - 0.48210 * h_rel ** 2 + 0.10420 * h_rel *
                             p_rel - 1.77400 * p_rel ** 2, 3))

    for n_0, n_1 in zip(n_rel_h, n_rel_l):
        n_rel.append(round(n_0 * n_1 * n_max, 3))
    return n_rel


if __name__ == '__main__':
    platform_len = 0.508
    d = 0.06
    p_max = 20
    p_n = 15
    p_rel = p_n / p_max
    n_max = 0.8
    x, y, z = catch_a_data('point_1.txt')
    n = calculate_efficiency(x, y, z)
    print(n)

    x, y, z = catch_a_data('point_2.txt')
    n = calculate_efficiency(x, y, z)
    print(n)

    x, y, z = catch_a_data('point_3.txt')
    n = calculate_efficiency(x, y, z)
    print(n)

    x, y, z = catch_a_data('point_4.txt')
    n = calculate_efficiency(x, y, z)
    print(n)
