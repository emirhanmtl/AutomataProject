# infix to postfix
def toPostfix(infix):
    stack = ""
    postfix = ""
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
            # Remove '(' from stack
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c

    while stack:
        postfix, stack = postfix + stack[-1], stack[:-1]

    return postfix

    while (not isEmpty(stack)):
        postfix += stack.pop()
    return postfix


# input symbols, transitions, initial-final state
class node:
    initial = None
    accept = None
    nodes = []

    def __init__(self, accept,initial):
        self.initial = initial
        self.accept = accept

# state oluşturma
class state:
    label = None
    edge1 = None
    edge2 = None

# postfix o nfa
def p2nfa(postfix):

    nfa = []

    def add(newNfa):
        newNFA = nfa(initial, accept)
        nfaStack.append(newNFA)
    for i in postfix:
        if i == ".":
            nfa_1 = nfa.pop()
            nfa_2 = nfa.pop()

            initial = state()
            initial.edge1 = nfa_1.append + nfa_2.append()

            newNFA = add(newNFA)
        if i =="|":
            nfa_1 = nfa.pop()
            nfa_2 = nfa.pop()

            initial = state()
            initial.edge1 = nfa_1.append()
            initial.edge2 = nfa_2.append()

            newNFA = add(newNFA)
        if i =="*":

            nfa_1 = nfa.pop()
            initial = state()
            initial.edge1 = nfa_1.initial()
            initial.edge2 = accept()

            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            newNFA = nfa(initial, accept)
            nfaStack.append(newNFA)
        else:
            accept = state()
            initial = state

            initial.label = "q" + i
            initial.edge1 = accept
            newNFA = add(newNFA)
    return nfa.pop()

#matching
def match(infix,string):
    postfix = toPostfix(infix)
    nfa = p2nfa(postfix)
    currentState = set
    currentState = nfa_iter(nfa.initial)

    for i in string:
        for k in postfix:
            if currentState == string[i]:
                print(currentState)

#following
def nfa_iter(infix,statE):
    postfix = toPostfix(infix)
    nfa = p2nfa(postfix)

    arrow = iter(nfa)

    if state.label is None:
        if state.edge1 is None:
            arrow = nfa_iter(state.edge1)
        elif state.edge2 is None:
            arrow = nfa_iter(state.edge2)
    return arrow



def main():
    infix = input("please enter an infix: ")
    string = input("please enter a string: ")


if __name__ == '__main__':
    main()














































