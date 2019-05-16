class Solution:
    def reverse(self, x: int) -> int:
        #x = -1 * int(str(x)[1:][::-1]) if x < 0 else int(str(x)[::-1])
        #return (x if x>-2**31 else 0) if x < 0 else (x if x<2**31 else 0)
        imax = 2_147_483_647
        imin = -2_147_483_648
        if x < imin or imax < x:
            return 0
        arr_rev = list(str(x))
        if arr_rev[0] == '-':
            arr_rev = arr_rev[1::]
            arr_rev += '-'
        arr_rev = arr_rev[::-1]
        y = int(''.join(arr_rev))
        if y < imin or y > imax:
            return 0
        return y

s = Solution()
print(s.reverse(123))
