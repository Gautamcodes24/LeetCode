class Solution:
    def isValid(self, s: str) -> bool:
        bra = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack = []
        for br in s:
            if br in bra.keys():
                # closing
                if stack and stack[-1] == bra[br]:
                    stack.pop()
                else:
                    stack.append(br)
            else:
                stack.append(br)
        return len(stack) == 0