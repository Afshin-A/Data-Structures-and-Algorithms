from Stack.Stack import Stack


def check_syntax(phrase):
    brackets = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    closing_brackets = brackets.keys()
    open_brackets = brackets.values()
    stack = Stack()
    
    for element in phrase:
        # if it's an open bracket, add it to the stack
        if element in open_brackets:
            stack.push(element)
        # if it's a closing bracket, we need to do some checks
        elif element in closing_brackets:
            # if stack is empty, we've reached a closing bracket for which there is no matching opening bracket, thus the syntax is incorrect
            if stack.isEmpty():
                return False
            else:
                # if the reverse of the closing bracket equals the element at the top of the stack, 
                if stack.pop() == brackets.get(element):
                    # syntax check pass for now ✅
                    continue
                else:
                    return False
        # if it's a character other than an open or closing bracket, ignore it
        else:
            continue
    
    # at this point, all elements have passed the check
    # if the stack is empty, the syntax is correct
    return stack.isEmpty()

'[({}[])]'