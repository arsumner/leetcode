I used two hash maps initialized using dictonary comprehension to map all unique values of the strings s and t. Before initializing these dicts, I compared the lengths of s and t - if they are not equal in length, then by default they are not anagrams. I then iteratered through both strings and stores counts as values for each key in the dicts. I iterated again through all values in s_dict to determine 1) if that letter in s existed in t and 2) if the counts were equal for all unique letters. If not, the function returns False.

Time complexity: O(n), or O(s+t), as both strings are iterated through
Space complexity: O(n), or O(s+t), as the memory that is used in the function is no more than the size of strings s and t combined.

Two other solutions I found that intrigued me:

return sorted(s) == sorted(t)

This is a simple one-liner, but time complexity is not as efficient here. Typically sorting requires at the worst a time complexity of O(n log n), which loses to the O(n) implementation. The tradeoff is that space complexity becomes (possibly) more efficient. In some built-ins, it can be as efficient as O(1), worst case O(n).

from collections import Counter
return Counter(s) == Counter(t)

This is just an interesting adoption from the collections library. It simply counts the elements of both s and t strings and returns true if equal. Space and time complexity here are O(n).