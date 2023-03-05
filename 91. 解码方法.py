"""
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。



示例 1：

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2：

输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
示例 3：

输入：s = "06"
输出：0
解释："06" 无法映射到 "F" ，因为存在前导零（"6" 和 "06" 并不等价）。


提示：

1 <= s.length <= 100
s 只包含数字，并且可能包含前导零。
"""
from utils import ensure


class Solution:
    def numDecodings(self, s: str) -> int:
        # f[i] 表示 s 的前 i 个字符 s[0..i-1] 的解码方法数
        # f[i] = f[i-1] + f[i-2]

        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]


class Test:

    @classmethod
    def test1(cls):
        s = "12"
        r = 2
        so = Solution()
        ensure(so.numDecodings(s), r, "测试 1")

    @classmethod
    def test2(cls):
        s = "226"
        r = 3
        so = Solution()
        ensure(so.numDecodings(s), r, "测试 2")

    @classmethod
    def test3(cls):
        s = "06"
        r = 0
        so = Solution()
        ensure(so.numDecodings(s), r, "测试 3")


def main():
    t = Test()
    t.test1()
    # t.test2()
    # t.test3()


if __name__ == '__main__':
    main()
