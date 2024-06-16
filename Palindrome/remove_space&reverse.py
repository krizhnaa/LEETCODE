
s = "tab a cat"

def isPalindrome(s):

    reversed = []
    org = []
    for ch in s[-1::-1]:
        if ch.isalnum():
            reversed.append(ch.lower())

    for ch in s:
        if ch.isalnum():
            org.append(ch.lower())

    return ''.join(org) == ''.join(reversed)


result = isPalindrome(s)
print(result)

