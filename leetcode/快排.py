def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def main():
    array = [1, 4, 6, 5, 3, 2]
    low, high = 0, len(array) - 1
    quick_sort(array, low, high)
    print("quick sort", array)


if __name__ == '__main__':
    main()
