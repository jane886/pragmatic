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


def log(*args):
    print(args)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩散法 这个思路最方便理解
        # 假设字符串长度超过3，则从第二个字符开始，往左右两边遍历，两两比较，直到遇到不同
        # 例如 [abcdcbx] 先从 b 开始 左边是 a 右边是 c 不满足
        # 接着是 c 左边是 b 右边是 d 不满足
        # 然后是 d 可以发现长度超过1的回文串
        # 需要注意的是 [abcddcma] 这种，需要在扩散的时候考虑中心相同的情况，所以可以走两次判断
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


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

