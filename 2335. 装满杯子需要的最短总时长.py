"""
现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。

给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。

示例 1：

输入：amount = [1,4,2]
输出：4
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。
示例 2：

输入：amount = [5,4,4]
输出：7
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。
示例 3：

输入：amount = [5,0,0]
输出：5
解释：每秒装满一杯冷水。


提示：

amount.length == 3
0 <= amount[i] <= 100

"""
from typing import List

from utils import ensure


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        a, b, c = amount
        # 每次装水，都尽量优先装满两个杯子

        # 当小杯和中杯的数量加起来小于或者等于大杯时，组合小大、中大杯，可以发现大杯的数量就是所需最少秒数
        if a + b <= c:
            return c
        # 当小杯和中杯的数量加起来大于大杯时，当小中组合装满到 n 杯后小于或大于大杯时，符合上面的条件，大杯数量加上 n 就是所需最少秒数
        else:
            n = a + b - c
            return n // 2 + c + n % 2


class Test:

    @classmethod
    def test1(cls):
        amount = [1, 4, 2]
        s = Solution()
        ensure(s.fillCups(amount), 4, "测试 1")

    @classmethod
    def test2(cls):
        amount = [5, 4, 4]
        s = Solution()
        ensure(s.fillCups(amount), 7, "测试 2")

    @classmethod
    def test3(cls):
        amount = [5, 0, 0]
        s = Solution()
        ensure(s.fillCups(amount), 5, "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
