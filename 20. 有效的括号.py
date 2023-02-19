"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false


提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""
from utils import ensure


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for c in s:
            if c in pairs:
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0


class Test:

    @classmethod
    def test1(cls):
        s = "()"
        r = True
        so = Solution()
        ensure(so.isValid(s), r, "测试 1")

    @classmethod
    def test2(cls):
        s = "()[]{}"
        r = True
        so = Solution()
        ensure(so.isValid(s), r, "测试 2")

    @classmethod
    def test3(cls):
        s = "(]"
        r = False
        so = Solution()
        ensure(so.isValid(s), r, "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
