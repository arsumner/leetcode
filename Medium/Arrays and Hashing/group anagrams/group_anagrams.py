from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = 26 * [0] # a-z

            for c in s:
                count[ord(c) - 97] += 1

            res[tuple(count)].append(s)

        return list(res.values())

test = Solution()
test.groupAnagrams(["ate", "rat", "tea"])
            