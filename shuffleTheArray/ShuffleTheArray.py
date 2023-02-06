class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        for xi, yi in zip(nums[:n], nums[n:]):
            result += [xi, yi]
        return result

    def test(self):
        tests = [
            [[2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]],
            [[1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]],
            [[1, 1, 2, 2], 2, [1, 2, 1, 2]],
        ]
        for test in tests:
            nums, n, expect_result = test
            result = self.shuffle(nums, n)
            print(result)
            print(result == expect_result)


if __name__ == '__main__':
    Solution().test()
