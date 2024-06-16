
s = "carrace"
t = "racecar"


def isAnagram(s, t):
    sHM, tHM = {}, {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        sHM[s[i]] = 1 + sHM.get(s[i], 0)
        tHM[t[i]] = 1 + tHM.get(t[i], 0)

    return sHM == tHM


result = isAnagram(s, t)
print(result)
