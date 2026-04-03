I used a hash map initialized with dictionary comprehension, mapping each unique value in nums as a key to 0. I then iterated through nums, and if a key's count was already 1, a duplicate was found and the function returns True immediately. This avoids unnecessary iteration. Otherwise the count is incremented.

Time complexity: O(n), as iteration through nums occurs once, with dictonary lookup/update time being O(1).
Space complexity: O(n), as hash map grows at most the size of nums.

I found another solution interesting:

seen = set()
for i in nums:
    if i in seen:
        return True
    seen.add(i)
return False

Here a hash set is used. Since there is no need to return any count, only True if a duplicate is found, key:value pairs are not crucial. Keys are added in this code, so that if a key has already been seen once, a duplicate is found.