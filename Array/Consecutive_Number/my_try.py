nums = [0,3,2,5,4,6,1,1]

def longestConsecutive(nums):
    nums.sort()
    no_dup = []
    for i in range(len(nums)):
        if i == 0 or nums[i - 1] != nums[i]:
            no_dup.append(nums[i])
    print(no_dup)

    consec_lst = []
    for i in range(len(no_dup)):
        if i == 0 and no_dup[i] + 1 == no_dup[i + 1]:
            consec_lst.append(no_dup[i])
        if no_dup[i - 1] + 1 == no_dup[i]:
            consec_lst.append(no_dup[i])

    return len(consec_lst)



result = longestConsecutive(nums)
print(result)