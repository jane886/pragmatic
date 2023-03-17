# 四个 int 型数组，给定一个 n，在每个数组里面取一个数，获取所有的满足和为 n 的排列。

class Solution(object):
    def fourSum(self, A, B, C, D, n):
        two_sum = {}
        res = []
        for a in A:
            for b in B:
                k = a + b
                if k not in two_sum:
                    two_sum[k] = [(a, b)]
                else:
                    two_sum[k].append((a, b))

        for c in C:
            for d in D:
                k = n - (c + d)
                if k in two_sum:
                    for i in two_sum[k]:
                        res.append(i + (c, d))
        return res


# 可以使用回溯法（backtracking）来解决这个问题，具体步骤如下：
# 定义一个函数backtrack，该函数接收四个参数：当前已经选择的数的个数count、当前已经选择的数的和sum、当前正在处理的数组index和目标和n，其中count和sum用来记录已经选取的数的个数和和值，index用来记录当前正在处理的数组的下标，n是目标和。
# 在backtrack函数中，首先判断当前已经选择的数的个数是否等于4，如果是，则判断当前已经选择的数的和是否等于n，如果是，则将当前选择的数的组合添加到结果列表中，否则直接返回。
# 如果当前已经选择的数的个数小于4，那么从第index个数组中选择一个数加入到当前已经选择的数的和中，并递归调用backtrack函数，将count加1，sum加上选择的数的值，index不变，n不变。
# 递归调用结束后，回溯到上一层调用，将选择的数从当前已经选择的数的和中去掉，将count和sum恢复到之前的值，index加1，继续从下一个数组中选择数并递归调用backtrack函数。
# 重复上述过程，直到处理完所有的数组。
# 以下是该算法的Python代码实现：
def fourSum(nums, target):
    result = []
    nums.sort()

    def backtrack(count, sum, index, target):
        if count == 4:
            if sum == target:
                result.append(list(combination))
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:  # 去重
                continue
            if nums[i] + sum > target:  # 剪枝
                break
            combination.append(nums[i])
            backtrack(count + 1, sum + nums[i], i + 1, target)
            combination.pop()

    combination = []
    backtrack(0, 0, 0, target)
    return result


# 其中，nums是四个int型数组，target是目标和，函数返回一个包含所有满足和为target的排列的列表。
def main():
    # 附赠测试用例：
    s = Solution()
    r = s.fourSum(
        [1, 2],
        [-2, -1],
        [-1, 2],
        [0, 2],
        n=0)
    print(r)

    # output: [(2, -1, -1, 0), (1, -2, -1, 2)]
    # 复杂度 O(N ^ 2)


if __name__ == '__main__':
    main()
