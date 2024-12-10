class Solution:
    def lengthOfLongestSubstring(s):
        seen = set()
        i = 0
        longest = 0

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i = i+1
            seen.add(s[j])
            longest = max(longest, j-i+1)
        return longest
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))