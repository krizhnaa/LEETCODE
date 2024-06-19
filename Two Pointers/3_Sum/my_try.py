
nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        if i != 0 and n == nums[i - 1]:
            continue
        else:
            target = -(n)
            l, r = i + 1, len(nums) - 1
            while (l < r):
                sum = nums[l] + nums[r]
                if sum == target:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l + 1] and l < r:
                        l += 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
    return res

result = threeSum(nums)
print(result)