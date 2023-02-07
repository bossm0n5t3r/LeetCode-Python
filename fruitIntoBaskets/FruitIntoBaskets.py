class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # Hash map 'basket' to store the types of fruits.
        basket = {}
        left = 0

        # Add fruit from the right index (right) of the window.
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            # If the current window has more than 2 types of fruit,
            # we remove one fruit from the left index (left) of the window.
            if len(basket) > 2:
                basket[fruits[left]] -= 1

                # If the number of fruits[left] is 0, remove it from the basket.
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

        # Once we finish the iteration, the indexes left and right
        # stands for the longest valid subarray we encountered.
        return right - left + 1

    def test(self):
        tests = [
            [[1, 2, 1], 3],
            [[0, 1, 2, 2], 3],
            [[1, 2, 3, 2, 2], 4],
            [[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5],
            [[0], 1],
        ]
        for test in tests:
            fruits, expect_result = test
            result = self.totalFruit(fruits)
            print(result)
            print(result == expect_result)


if __name__ == '__main__':
    Solution().test()
