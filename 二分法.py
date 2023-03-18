def binary_search(array, target):
    array.sort()
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


def main():
    array = [1, 40, 20, 80, 10, 100]
    target = 100
    index = binary_search(array, target)
    print("index", index)


if __name__ == '__main__':
    main()
