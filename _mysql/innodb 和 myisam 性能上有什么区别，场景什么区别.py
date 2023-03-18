"""


InnoDB 和 MyISAM 性能上有什么区别，场景什么区别

    InnoDB 和 MyISAM 在性能方面的区别如下：
    1，读写性能：在读写方面，MyISAM 的性能优于 InnoDB，因为 MyISAM 采用表级锁定，对于大量的读操作，可以提高并发性能。
     而 InnoDB 采用行级锁定，对于大量的写操作，可以提高并发性能。
     因此，在读多写少的应用中，MyISAM 更适合；
     在读写操作比较均衡的应用中，InnoDB 更适合

    2，并发性能：在并发方面，InnoDB 的性能优于 MyISAM，因为 InnoDB 采用行级锁定和缓冲池机制，可以提高并发性。
     而 MyISAM 采用表级锁定和操作系统级别的缓存机制，容易造成锁定等待和死锁。因此，在并发读写较高的应用中，InnoDB 更适合

    3，整体性能：在整体性能方面，InnoDB 的性能优于 MyISAM，因为 InnoDB 支持事务处理，外间关联等高级功能，可以保证数据的完整性和一致性。
     同时，InnoDB 支持 B+ 树索引结构和缓冲池机制，可以提高查询性能和排序性能。而 MyISAM 不支持这些高级功能，所以在可靠性和性能方面都不如 InnoDB

    在选择存储引擎时，需要根据应用程序的特点和需求来进行选择。如果应用程序需要高并发和高读写性能，可以选择 MyISAM；
    如果应用程序


"""

import time


def record_time(func):
    def log(*args, **kwargs):
        start = int(time.time() * 1000)
        res = func(*args, **kwargs)
        end = int(time.time() * 1000)
        print(f"记录时长:{end - start} ms")
        return res

    return log


@record_time
def _add(a, b):
    print("klui")
    time.sleep(1)
    print("jxuu")
    return a + b


def partition(array, low, high):
    i = low - 1
    pi = array[high]
    for j in range(low, high):
        if array[j] <= pi:
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
    array = [1, 5, 4, 6, 9, 3, 2]
    low, high = 0, len(array) - 1
    quick_sort(array, low, high)
    print(array)


if __name__ == '__main__':
    main()
