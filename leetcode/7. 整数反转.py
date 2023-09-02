"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−2**31,  2 ** 31 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0


提示：

-231 <= x <= 231 - 1

"""
from utils import ensure


class Solution:
    def reverse(self, x: int) -> int:
        n = int(str(abs(x))[::-1])
        if x < 0:
            n = -n
        return n if -2**31 < n < 2**31 - 1 else 0


class Test:

    @classmethod
    def test1(cls):
        x = 123
        r = 321
        so = Solution()
        ensure(so.reverse(x), r, "测试 1")

    @classmethod
    def test2(cls):
        x = -123
        r = -321
        so = Solution()
        ensure(so.reverse(x), r, "测试 2")

    @classmethod
    def test3(cls):
        x = 120
        r = 21
        so = Solution()
        ensure(so.reverse(x), r, "测试 3")

    @classmethod
    def test4(cls):
        x = 0
        r = 0
        so = Solution()
        ensure(so.reverse(x), r, "测试 4")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()
    t.test4()


if __name__ == '__main__':
    main()
