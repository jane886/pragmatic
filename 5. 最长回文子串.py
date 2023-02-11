"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""
from utils import ensure


class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


class Test:

    @classmethod
    def test1(cls):
        s = "babad"
        so = Solution()
        ensure(so.longestPalindrome(s), "bab", "测试 1")

    @classmethod
    def test2(cls):
        s = "cbbd"
        so = Solution()
        ensure(so.longestPalindrome(s), "bb", "测试 2")


def main():
    t = Test()
    t.test1()
    t.test2()


if __name__ == '__main__':
    main()

