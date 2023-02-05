class Solution:
    @staticmethod
    def make_anagram_list(s):
        result = [0] * 26
        for c in s:
            result[ord(c) - ord('a')] += 1
        return result

    def findAnagrams(self, s: str, p: str) -> list[int]:
        target_anagram_list = self.make_anagram_list(p)
        tmp = self.make_anagram_list(s[:len(p)])
        result = []
        if tmp == target_anagram_list:
            result.append(0)
        for i in range(1, len(s) - len(p) + 1):
            tmp[ord(s[i - 1]) - ord('a')] -= 1
            tmp[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if tmp == target_anagram_list:
                result.append(i)
        return result

    def test(self):
        tests = [
            ["cbaebabacd", "abc", [0, 6]],
            ["abab", "ab", [0, 1, 2]],
        ]
        for test in tests:
            s, p, expect_result = test
            result = self.findAnagrams(s, p)
            print(result)
            print(result == expect_result)


if __name__ == '__main__':
    Solution().test()
