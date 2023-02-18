"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

例如，121 是回文，而 123 不是。


示例 1：

输入：x = 121
输出：true
示例 2：

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。


提示：

-231 <= x <= 231 - 1


进阶：你能不将整数转为字符串来解决这个问题吗？
"""
from utils import ensure


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        result = 0
        index = 10
        while x > result:
            result = result * index + x % index
            x //= index
        return x == result or x == result // 10


class Test:

    @classmethod
    def test1(cls):
        x = 121
        r = True
        so = Solution()
        ensure(so.isPalindrome(x), r, "测试 1")

    @classmethod
    def test2(cls):
        x = -121
        r = False
        so = Solution()
        ensure(so.isPalindrome(x), r, "测试 2")

    @classmethod
    def test3(cls):
        x = 10
        r = False
        so = Solution()
        ensure(so.isPalindrome(x), r, "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
