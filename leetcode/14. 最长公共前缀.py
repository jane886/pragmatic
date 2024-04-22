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
    # 横向扫描
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]


# 复杂度分析

    # 时间复杂度：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。
        # 最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。

    # 空间复杂度：O(1)。使用的额外空间复杂度为常数。


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
