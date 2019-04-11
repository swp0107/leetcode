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

    def withoutMemory(self, s: str) -> int:
        i = j = l = 0
        for j, c in enumerate(s):
            if c in s[i:j]:
                l = max(l, len(s[i:j]))
                i += s[i:j].index(c)+1
            return max(l, len(s[i:j+1]))

s = Solution()
print(s.legnthOfLongestSubstring("abcabcbb"))
print(s.legnthOfLongestSubstring("bbbbb"))
print(s.legnthOfLongestSubstring("pwwkew"))

print(s.withoutMemory("abcabcbb"))
print(s.withoutMemory("bbbb"))
print(s.withoutMemory("pwwkew"))
