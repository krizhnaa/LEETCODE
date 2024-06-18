
s = "[()]"

def isValid(s):
    stack = []
    hashMap = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket not in hashMap:
            stack.append(bracket)
            continue

        if not stack or stack[-1] != hashMap[bracket]:
            return False

        stack.pop()
    return not stack


result = isValid(s)
print(result)

