nums = [1,2,3,1]


def has_duplicate(nums):
    nums.sort()

    for n in range(len(nums) - 1):
        if nums[n] == nums[n + 1]:
            return True

    return False


result = has_duplicate(nums)
print(result)