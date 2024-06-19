numbers = [1,2,3,4]
target = 3


def twoSum(nums, target):
    l, r = 0, len(nums) - 1

    while (l < r):
        sum = nums[l] + nums[r]
        if sum == target:
            break
        elif sum < target:
            l += 1
        else:
            r -= 1
    return [l + 1, r + 1]


result = twoSum(numbers, target)
print(result)