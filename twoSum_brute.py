def twoSum(nums, target):
    sol = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if (i == j):
                continue
            if (nums[i] + nums[j] == target):
                sol.append(i)
                sol.append(j)
                return (sol)


x = list(map(int, input().split()))
t = int(input())

print(twoSum(x, t))
