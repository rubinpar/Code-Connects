from queue import LifoQueue


# Put things in a stack
stack = LifoQueue()
# stack.put(thing)
# stack.get()

stack.put("box1")
stack.put("box2")
stack.put("box3")
stack.put("box4")

def print_stack(stack):
    remainders = LifoQueue()
    while not stack.empty():
        top_thing = stack.get()
        print(top_thing)
        remainders.put(top_thing)
    while not remainders.empty():
        stack.put(remainders.get())

def reverse(stack):
    """
    Gives you the stack in reverse order
    """
    new_stack = LifoQueue()
    while not stack.empty():
        top_thing = stack.get()
        new_stack.put(top_thing)
    return new_stack

print_stack(reverse(stack))


# is_balanced("()") -> True
# is_balanced("(()))") -> False`
def is_balanced(parens: str) -> bool:
    stack = LifoQueue()
    balanced = True
    index = 0
    while index < len(parens) and balanced:
        symbol = parens[index]
        if symbol == "(":
            stack.put(symbol)
        else: # symbol == ")"
            if stack.empty():
                balanced = False
            else:
                stack.get()
        index += 1

    return balanced and stack.empty()

print(is_balanced("()"))  # True
print(is_balanced("(()()")) # False
print(is_balanced("(((())")) # False
print(is_balanced("()(()(()))")) # True
