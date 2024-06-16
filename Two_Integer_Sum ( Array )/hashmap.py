# TC : O(n)

nums = [2, 3, 5, 7]
target = 10


def twoSum(nums, target):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


result = twoSum(nums, target)
print(result)