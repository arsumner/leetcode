There are a couple of implementation paths that can be taken here: sorting and not sorting. Sorting would take O(nlogn), but to achieve O(n) time commplexity, sorting should not take place first. In this implementation, the list of strings is iterated through. A dictionary called res is initialized using defaultdict() from the collections library to store the lists of anagrams. 

A count list is initialized inside the for loop for the strs list iteration and set to a lenth of 26, where each index is set to 0. This count list stores the count for each character in each string - a-z. Each string is iterated through character by character and counts are added to the count list representing that char's position in the 26 letter alphabet.

NOTE: ord(c) is used to find the ASCII value of each letter. In order to index this from 0-25 (26 chars total), we must use the equation: ord(c) - 97. 97 is the ASCII value of the letter "a". Another approach would be to do: ord(c) - ord("a").

After iteration through a string, the count list is appended to the res dict. Because lists are mutable and cannot be keys in a dict, we perform a type change res[tuple(count)], as tuples are immutable and therefore can be dictionary keys. By using the collections function defaultdict(list), there will not be keyerrors if the key is the first to enter the dict (i.e. not appended to an existing list already in the dict). 

At the end, the res dict's values are returned, where the values are lists of anagrans ([rat], [ate, tea]). To ensure that a dict isn't retuned we use: return list(res.values()).

Time complexity: O(n * m), where m is the length of the longest string and n is the length of the strs list, as iteration must be completed through the strs lists and each individual string's chars.

Space complexity: O(n * m), as all chars across all strings are being stored