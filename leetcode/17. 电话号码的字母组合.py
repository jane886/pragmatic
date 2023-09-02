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
