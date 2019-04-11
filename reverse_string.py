class Solution:
    def reverseString(self, s) -> None:
        i = 0
        j = len(s)-1
        while (i <= j):
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1

s = Solution()
h = "Hello"
h = list(h)
print(h)
s.reverseString(h)
print(h)
