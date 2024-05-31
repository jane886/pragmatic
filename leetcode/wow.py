# 问题：https://codeforces.com/contest/1178/problem/B

def parse_wow(string):
    offset = 0
    count = 0
        # 记录第一次遍历到 o 的坐标
    first_o_index = -1
        # 记录第一次遍历到 o 的坐标的时候，坐标左边和右边分别的 w 个数
    first_o_left_w_count, first_o_right_w_count = 0, 0
    while offset < len(string):
        ele = string[offset]
        if ele == "o":
                # 第一次遍历到 o，分别计算坐标左右两边的 w 的次数，然后相乘就能得到第一个拼接 wow 的个数
            if first_o_index < 0:
                left, right = string[:offset], string[offset+1:]
                w_count_left, w_count_right = find_w(left), find_w(right)
                count += w_count_left * w_count_right
                    # 记录此时 o 的坐标和左右两边的可以拼接的 w 个数
                first_o_index = offset
                first_o_left_w_count, first_o_right_w_count = w_count_left, w_count_right
            else:
                    # 以后的每次遍历 o，只需要计算第一次 o 坐标和当前 o 坐标到之间的字符串有多少 w
                    # 然后用初始左边 w 数加上中间 w 数，初始右边 w 数减去中间 w 数
                mid = string[first_o_index:offset]
                c = find_w(mid)
                count += (first_o_left_w_count + c) * (first_o_right_w_count - c)

        offset += 1
    return count


def find_w(string):
    offset = 0
    count = 0
    while offset < len(string):
        ele_2 = string[offset: offset + 2]
        if ele_2 == "vv":
            count += 1
        offset += 1
    return count


def __main():
    pass
    s1 = "vvvovvv"
    r1 = 4
    w1 = parse_wow(s1)
    print("w1", w1, w1 == r1)

    s2 = "vvovooovovvovoovoovvvvovovvvov"
    r2 = 100
    w2 = parse_wow(s2)
    print("w2", w2, w2 == r2)


if __name__ == '__main__':
    __main()
