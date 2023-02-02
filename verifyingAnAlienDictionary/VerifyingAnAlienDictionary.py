class Solution:
    def isAlienSorted(self, words, order) -> bool:
        def is_alien_ordered(word1, word2, order2dict):
            min_length = min(len(word1), len(word2))
            for i in range(min_length):
                if order2dict[word1[i]] < order2dict[word2[i]]:
                    return True
                elif order2dict[word1[i]] > order2dict[word2[i]]:
                    return False
            if len(word1) > len(word2):
                return False
            return True

        order_dict = {order[i]: i for i in range(len(order))}
        for i in range(len(words) - 1):
            cur_word, next_word = words[i], words[i + 1]
            if not is_alien_ordered(cur_word, next_word, order_dict):
                return False
        return True

    def test(self):
        tests = [
            [
                ["hello", "leetcode"],
                "hlabcdefgijkmnopqrstuvwxyz",
                True,
            ],
            [
                ["word", "world", "row"],
                "worldabcefghijkmnpqstuvxyz",
                False,
            ],
            [
                ["apple", "app"],
                "abcdefghijklmnopqrstuvwxyz",
                False,
            ],
        ]
        for test in tests:
            words, order, test_result = test
            result = self.isAlienSorted(words, order)
            print(result == test_result)


if __name__ == '__main__':
    Solution().test()
