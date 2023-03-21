def min_value_of_abs(array):
    if array[0] >= 0:
        return array[0]

    if array[-1] <= 0:
        return array[-1]

    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > 0:
            if array[mid - 1] < 0:
                return array[mid] if abs(array[mid]) < abs(array[mid - 1]) else abs(array[mid - 1])
            high = mid - 1
        elif array[mid] < 0:
            low = mid + 1
        else:
            return array[mid]
    return None


def main():
    # 求一个有序数组中绝对值最小的值
    a = [-3, -2, -1, 1, 5, 7]
    print(min_value_of_abs(a))


if __name__ == '__main__':
    main()
