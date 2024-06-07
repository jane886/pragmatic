"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

"""
from typing import List

from utils import ensure


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(offset):
            if offset == len(digits):
                combinations.append(''.join(combination))
            else:
                d = digits[offset]
                for letter in phone_map[d]:
                    combination.append(letter)
                    backtrack(offset + 1)
                    combination.pop()

        combination = []
        combinations = []
        backtrack(0)
        return combinations


# 方法一：回溯
# 首先使用哈希表存储每个数字对应的所有可能的字母，然后进行回溯操作。

# 回溯过程中维护一个字符串，表示已有的字母排列（如果未遍历完电话号码的所有数字，则已有的字母排列是不完整的）。
# 该字符串初始为空。每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母，并将其中的一个字母插入到已有的字母排列后面，然后继续处理电话号码的后一位数字，直到处理完电话号码中的所有数字，即得到一个完整的字母排列。然后进行回退操作，遍历其余的字母排列。

# 回溯算法用于寻找所有的可行解，如果发现一个解不可行，则会舍弃不可行的解。
# 在这道题中，由于每个数字对应的每个字母都可能进入字母组合，因此不存在不可行的解，直接穷举所有的解即可。


# 该算法的时间复杂度为O(3^N × 4^M)，其中N是输入数字字符串中对应3个字母的数字数量，M是输入数字字符串中对应4个字母的数字数量。
# 空间复杂度为O(3^N × 4^M)，用于存储结果列表。


class Test:

    @classmethod
    def test1(cls):
        digits = "23"
        r = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        so = Solution()
        ensure(so.letterCombinations(digits), r, "测试 1")

    @classmethod
    def test2(cls):
        digits = ""
        r = []
        so = Solution()
        ensure(so.letterCombinations(digits), r, "测试 2")

    @classmethod
    def test3(cls):
        digits = "2"
        r = ["a", "b", "c"]
        so = Solution()
        ensure(so.letterCombinations(digits), r, "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
