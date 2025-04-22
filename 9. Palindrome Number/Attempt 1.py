class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        return x == x[::-1]


sol = Solution()
print(sol.isPalindrome(1221))