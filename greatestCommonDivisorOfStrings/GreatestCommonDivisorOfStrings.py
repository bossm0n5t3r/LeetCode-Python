class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(expect_divisor, target):
            if len(expect_divisor) > len(target):
                return False
            if len(target) % len(expect_divisor) != 0:
                return False
            return target == (expect_divisor * (len(target) // len(expect_divisor)))

        if len(str1) > len(str2):
            str1, str2 = str2, str1

        for i in range(len(str1), 0, -1):
            divisor = str1[:i]
            if is_divisor(divisor, str1) and is_divisor(divisor, str2):
                return divisor
        return ""

    def test(self):
        tests = [
            ["ABCABC", "ABC", "ABC"],
            ["ABABAB", "ABAB", "AB"],
            ["LEET", "CODE", ""],
            ["", "CODE", ""],
            ["LEET", "", ""],
        ]
        for test in tests:
            str1, str2, test_result = test
            result = self.gcdOfStrings(str1, str2)
            print(result == test_result)


if __name__ == '__main__':
    Solution().test()
