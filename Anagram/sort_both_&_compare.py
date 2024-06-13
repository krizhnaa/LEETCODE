
# Also can use hashmap, which keeps the character of each string with their occurences

s = "carrace"
t = "racecar"

def isAnagram(s, t):
    sorted_s, sorted_t = ''.join(sorted(s)), ''.join(sorted(t))

    if sorted_s == sorted_t:
        return True
    else:
        return False

result = isAnagram(s, t)
print(result)


