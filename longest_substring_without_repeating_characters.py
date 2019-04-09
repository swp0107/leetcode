class Solution:
    def legnthOfLongestSubstring(self, s: str) -> int:
        m = []
        l = 0
        for c in s:
            if c in m:
                l = max(l, len(m))
                m = m[m.index(c)+1:]
            m.append(c)
        return (max(l, len(m)))


s = Solution()
print(s.legnthOfLongestSubstring("abcabcbb"))
print(s.legnthOfLongestSubstring("bbbbb"))
print(s.legnthOfLongestSubstring("pwwkew"))
