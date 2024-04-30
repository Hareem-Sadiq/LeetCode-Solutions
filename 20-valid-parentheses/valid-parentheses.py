class Solution(object):
    def isValid(self, s):
        char = []
        for parenthesis in s:
            if parenthesis in ['(' ,'[' ,'{']:
                char.append(parenthesis)
            else:
                if not char:
                    return False
                else:
                    top = char[-1]
                if parenthesis == ')':
                    if top == '(':
                        char.pop()
                    else:
                        return False
                elif parenthesis == ']':
                    if top == '[': 
                        char.pop()
                    else:
                        return False
                elif parenthesis == '}':
                    if top == '{':
                        char.pop()
                    else:
                        return False
        return not char