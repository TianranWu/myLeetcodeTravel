class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            "(":")",
            "{":"}",
            "[":"]",
        }
        
        stack = list()
        for i in range(len(s)):
            if stack == []:
                stack.append(s[i])
                continue

            if s[i] == ")" and stack[-1] == "(":
                stack.pop()
            elif s[i] == "]" and stack[-1] == "[":
                stack.pop()
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(s[i])
            # print(stack)

        return True if stack == [] else False
