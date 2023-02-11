"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""
from utils import ensure


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 开始遍历，用 element 记录已经遍历过的元素，
        # 当前元素如果未出现在记录中，添加
        # 如果出现过，记录当前 element 的长度，组合当前元素，找到当前元素最早出现的下标，element 截取为下标 + 1 后面的元素
        # 最后要再检查下 element 的长度
        length = 0
        offset = 0
        element = ''
        while offset < len(s):
            # print(f"element:{element}", f"目前最长距离:{length}")
            e = s[offset]
            # print(f"当前元素:{e}", f"组合元素:{element + e}")
            # print(f"出现重复:{e in element}")
            if e not in element:
                element += e
            else:
                length = len(element) if len(element) > length else length
                element += e
                index = element.index(e)
                # print(f"元素在第{index}坐标")
                element = element[index + 1:]
            offset += 1
            # print(f"--------------")

        length = len(element) if len(element) > length else length
        return length


class Test:

    @classmethod
    def test1(cls):
        s = "abcabcbb"
        so = Solution()
        ensure(so.lengthOfLongestSubstring(s), 3, "测试 1")

    @classmethod
    def test2(cls):
        s = "!b"
        so = Solution()
        ensure(so.lengthOfLongestSubstring(s), 2, "测试 2")

    @classmethod
    def test3(cls):
        s = "pwwkew"
        so = Solution()
        ensure(so.lengthOfLongestSubstring(s), 3, "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
