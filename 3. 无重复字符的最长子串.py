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
        # 1. 定义左右指针
        # 2. 定义最大长度
        # 3. 定义最大字符串
        # 4. 定义字符集合
        # 5. 遍历字符串
        # 6. 如果当前字符不在字符集合中，则将当前字符加入字符集合，右指针右移
        # 7. 如果当前字符在字符集合中，则将左指针右移，直到当前字符不在字符集合中
        # 8. 如果当前字符不在字符集合中，则将当前字符加入字符集合，右指针右移
        # 9. 如果当前字符在字符集合中，则将左指针右移，直到当前字符不在字符集合中
        # 10. 重复 6-9
        # 11. 返回最大长度
        left = right = 0
        max_len = 0
        char_set = set()
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                if right - left > max_len:
                    max_len = right - left
            else:
                char_set.remove(s[left])
                left += 1
        return max_len


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
