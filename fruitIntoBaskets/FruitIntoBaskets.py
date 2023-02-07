class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        result = 0
        tmp_fruits = set()
        before_fruit = -1
        for i in range(len(fruits)):
            first_fruit = fruits[i]
            second_fruit = -1
            if before_fruit == first_fruit:
                continue
            baskets = {first_fruit: 1}
            for j in range(i + 1, len(fruits)):
                tmp = fruits[j]
                if tmp == first_fruit:
                    baskets[first_fruit] += 1
                elif second_fruit == -1:
                    second_fruit = tmp
                    baskets[second_fruit] = 1
                    if tmp_fruits == {first_fruit, second_fruit}:
                        break
                elif tmp == second_fruit:
                    baskets[second_fruit] += 1
                else:
                    break
            all_fruits_in_baskets = baskets[first_fruit]
            if second_fruit != -1:
                all_fruits_in_baskets += baskets[second_fruit]
            if all_fruits_in_baskets > result:
                result = all_fruits_in_baskets
                tmp_fruits = {first_fruit, second_fruit}
            before_fruit = first_fruit
        return result

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
