
s = "Was it a car or a cat I saw?"

def isPalindrome(s):

    str = ""
    for ch in s:
        if ch.isalnum():
            str += ch.lower()

    return str == str[-1::-1]


result = isPalindrome(s)
print(result)

