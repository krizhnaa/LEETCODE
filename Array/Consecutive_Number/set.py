nums = [0,3,2,5,4,6,1,1]

def longestConsecutive(nums):

    numSet = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in numSet:
            length = 0
            while ( n + length) in numSet:
                length += 1
                longest = max(longest, length)
    return longest



result = longestConsecutive(nums)
print(result)