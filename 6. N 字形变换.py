"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);


示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R

示例 2：
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
示例 3：

输入：s = "A", numRows = 1
输出："A"


提示：

1 <= s.length <= 1000
s 由英文字母（小写和大写）、',' 和 '.' 组成
1 <= numRows <= 1000
"""
from utils import ensure


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        result = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            result[i] += c
            flag = -flag if i == 0 or i == numRows - 1 else flag
            i += flag
        return ''.join(result)


class Test:

    @classmethod
    def test1(cls):
        s = "PAYPALISHIRING"
        numRows = 3
        r = "PAHNAPLSIIGYIR"
        so = Solution()
        ensure(so.convert(s, numRows), r, "测试 1")

    @classmethod
    def test2(cls):
        s = "PAYPALISHIRING"
        numRows = 4
        r = "PINALSIGYAHRPI"
        so = Solution()
        ensure(so.convert(s, numRows), r, "测试 2")

    @classmethod
    def test3(cls):
        s = "A"
        numRows = 1
        r = "A"
        so = Solution()
        ensure(so.convert(s, numRows), r, "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
