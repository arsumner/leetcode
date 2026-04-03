class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = {n: 0 for n in s}, {n: 0 for n in t}

        for i in s:
            s_dict[i] += 1
        for i in t:
            t_dict[i] += 1
        for i in s_dict:
            if i not in t_dict or t_dict[i] != s_dict[i]:
                return False
        return True