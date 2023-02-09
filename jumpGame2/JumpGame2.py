class Solution:
    def jump(self, nums: list[int]) -> int:
        queue = []
        visited = [False] * len(nums)

        step = 0
        queue.append(0)
        visited[0] = True

        while queue:
            size = len(queue)
            while size:
                cur_index = queue.pop(0)
                if cur_index == len(nums) - 1:
                    return step
                visited[cur_index] = True
                for j in range(nums[cur_index] + 1):
                    next_index = cur_index + j
                    if next_index >= len(nums) or visited[next_index]:
                        continue
                    queue.append(next_index)
                    visited[next_index] = True
                size -= 1
            step += 1
        return -1

    def test(self):
        tests = [
            [[2, 3, 1, 1, 4], 2],
            [[2, 3, 0, 1, 4], 2],
        ]
        for test in tests:
            nums, expect_result = test
            result = self.jump(nums)
            print(result)
            print(result == expect_result)


if __name__ == '__main__':
    Solution().test()
