"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。



示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


提示：

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

"""
from typing import List

from utils import ensure


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        current = strs[0]
        for s in strs[1:]:
            current = self.compare(current, s)

        return current

    @staticmethod
    def compare(s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        s = ''
        for i, c in enumerate(s1):
            if c == s2[i]:
                s += c
            else:
                break
        return s


class Test:

    @classmethod
    def test1(cls):
        s = ["flower", "flow", "flight"]
        r = "fl"
        so = Solution()
        ensure(so.longestCommonPrefix(s), r, "测试 1")

    @classmethod
    def test2(cls):
        s = ["dog", "racecar", "car"]
        r = ''
        so = Solution()
        ensure(so.longestCommonPrefix(s), r, "测试 2")


def main():
    t = Test()
    t.test1()
    t.test2()


if __name__ == '__main__':
    main()
