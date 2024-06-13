# Time complexity is O(n^2)

nums = [2, 1, 5, 3]
target = 7

def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1):
            j+=1
            if nums[i] + nums[j] == target:
                return [i, j]
    return "no result"


result = twoSum(nums, target)
print(result)