class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        n = len(s)

        for i in range(n):
            for j in range(i + 1, n+1):

                sub = s[i:j]

                if sub == sub[::-1]:
                    if len(sub) > len(longest):
                        longest = sub

        return longest