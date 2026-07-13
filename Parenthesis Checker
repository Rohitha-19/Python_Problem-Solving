class Solution:
    def isBalanced(self, s):
        stack = []
        for ch in s:
            # Opening brackets
            if ch in "({[":
                stack.append(ch)
            # Closing brackets
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (ch == ')' and top != '(') or \
                   (ch == '}' and top != '{') or \
                   (ch == ']' and top != '['):
                    return False
        return len(stack) == 0
