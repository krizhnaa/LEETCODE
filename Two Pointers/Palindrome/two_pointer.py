
s = "Was it a car or a cat I saw?"

def isPalindrome(s):

    l, r = 0, len(s) - 1

    while (l < r):

        if l < r and not s[l].isalnum():
            l +=1

        if r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


result = isPalindrome(s)
print(result)