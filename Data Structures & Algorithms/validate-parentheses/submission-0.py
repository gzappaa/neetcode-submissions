class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashes = {')':'(', '}' : '{', ']' : '['}

        for ch in s:
            if ch in hashes:
                if stack and stack[-1] == hashes[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return stack == []

            