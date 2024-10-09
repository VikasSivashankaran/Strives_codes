s = "babad"
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(word):
            return word == word[::-1]
        
        longest = ""

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if isPalindrom(s[i:j]) and len(s[i:j]) > len(longest):
                    longest = s[i:j]
        return longest
sol = Solution()

result = sol.longestPalindrome(s)
print(result)