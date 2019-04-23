class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		output = ''

		# Make a table to store information whether [Si,...Sj] is a palindrome
		table = [[0 for x in range(n)] for y in range(n)]

		# All substring of length 1 are palindromes
		if n >= 1:
			for i in range(n):
				table[i][i] = True
				output = s[i]

		# check for substrings of length 2
		if n >= 2:
			for j in range(n - 1):
				if s[j] == s[j + 1]:
					table[j][j+1] = True
					output = s[j:j+2]
		# check for substrings of length greater than 2
		if n >= 3:
			for k in range(3, n+1):
				for a in range (0, n + 1 - k):
					if s[a] == s[a + k - 1] and table[a + 1][a + k - 2] == True:
						table[a][a + k - 1] = True
						output = s[a:a+k]

		return output
