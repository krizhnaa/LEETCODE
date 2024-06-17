strs = ["act","pots","tops","cat","stop","hat"]


def groupAnagram(strs):

    final_lst = []
    if len(strs) < 2:
        final_lst.append(strs)
    else:
        for str in strs:
            lst = []
            lst.append(str)

            hM1 = {}

            for ch in range(len(str)):
                hM1[str[ch]] = 1 + hM1.get(str[ch], 0)

            for i in strs[strs.index(str)+1:]:
                if len(str) == len(i):
                    hM2 = {}
                    for c in range(len(i)):
                        hM2[i[c]] = 1 + hM2.get(i[c], 0)
                    if hM1 == hM2:
                        lst.append(i)
                        strs.remove(i)

            final_lst.append(lst)
        i = 0
        while(i<len(final_lst)):
            for ele in range(len(final_lst) - 1):
                if len(final_lst[ele]) > len(final_lst[ele + 1]):
                    temp = final_lst[ele]
                    final_lst[ele] = final_lst[ele + 1]
                    final_lst[ele + 1] = temp
                i+=1
    return final_lst

result = groupAnagram(strs)
print(result)