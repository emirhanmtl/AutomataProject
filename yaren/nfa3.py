star = '*'
line = '|'
dot = '·'
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + \
    [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
    [chr(i) for i in range(ord('0'), ord('9') + 1)]
startState = None
finalState = None
states = set()


class nfa:
    accept = None
    initial = None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept


def setStart(self, state):
    self.startState = state
    self.states.add(state)


def addFinal(self, state):
    if isinstance(state, int):
        state = [state]
    for s in state:
        if s not in self.finalState:
            self.finalState.append(s)


# infix to postfix
def toPostfix(infix):
    specials = {'?': 70, '+': 60, '*': 50, '.': 40, '|': 30}
    stack = ""
    postfix = ""
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
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


class State:
    label = None
    edge1 = None
    edge2 = None
    def __init__(self, name):
        self.epsilon = []  # epsilon-closure
        self.transitions = {}  # char : state
        self.name = name
        self.is_end = False

def compile(postfix):
    nfaStack = []

    for c in postfix:
        if c == star:
            # Pop a single NFA from the stack
            nfa1 = nfaStack.pop()

            # Create new initial and accept states
            initial = State()
            accept = State()

            # Join the new initial state to nfa1's initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            # Join the old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept

            # Push new NFA to the stack
            newNFA = nfa(initial, accept)
            nfaStack.append(newNFA)
        elif c == dot:
            # Pop two NFAs off the stack
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            # Connect first NFA's accept state to the second's initial
            nfa1.accept.edge1 = nfa2.initial

            # Push new NFA to the stack
            newNFA = nfa(nfa1.initial, nfa2.accept)
            nfaStack.append(newNFA)
        elif c == line:
            # Pop two NFAs off the stack
            nfa2 = nfaStack.pop()
            nfa1 = nfaStack.pop()

            # Create a new initial state, connect it to initial states
            # of the two NFAs popped from the stack
            initial = State()

            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            # Create a new accept state, connecting the accept states
            # of the two NFAs popped from the stack to the new state
            accept = State()

            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            # Push new NFA to the stack
            newNFA = nfa(initial, accept)
            nfaStack.append(newNFA)
        else:
            # Create new initial and accept states
            accept = State()
            initial = State()

            # Join the initial state and the accept state using an arrow labelled 'c'
            initial.label = c
            initial.edge1 = accept

            # Push new NFA to the stack
            newNFA = nfa(initial, accept)
            nfaStack.append(newNFA)

    # NFA stack should only have a single NFA on it at this point
    return nfaStack.pop()


def followArrowE(state):
    # Create a new set, with each state as it's only member
    states = set()
    states.add(state)

    # Check if state has arrows labelled 'e' from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # If there's an edge1, follow it
            states |= followArrowE(state.edge1)
        # Check if edge2 is a state
        if state.edge2 is not None:
            # If there's an edge2, follow it
            states |= followArrowE(state.edge2)

    # Return the set of states
    return states


def match(infix, string):
    # Shunt and compile the regular expression
    postfix = toPostfix(infix)
    nfa = compile(postfix)

    # The current set of states and the next set of states
    currentState = set()
    nextState = set()

    # Add the initial state to the current set of states
    currentState |= followArrowE(nfa.initial)

    # Loop through each character in the string
    for s in string:
        # Loop through current set of states
        for c in currentState:
            # Check if that state is labelled 's'
            if c.label == s:
                # Add edge1 state to the next set of states
                nextState |= followArrowE(c.edge1)

        # Set currentState to next and clear out nextState
        currentState = nextState
        nextState = set()

    # Check if the accept state is in the current set of states
    return (nfa.accept in currentState)

class NFA:
    def __init__(self, start, end, ):
        self.state_set = []
        self.alphabet = []
        self.start = start
        self.end = end  # start and end states
        end.is_end = True
        self.transitions = []
class Handler:
    def __init__(self):
        self.state_count = 0

    def create_state(self):
        self.state_count += 1
        return State('q' + str(self.state_count))
    def handle_char(self, t, nfa_stack):
        s0 = self.create_state()
        s1 = self.create_state()
        s0.transitions[t] = s1
        nfa = NFA(s0, s1)
        if t not in alphabet:
            nfa.alphabet.append(t)
        nfa.state_set.append(s0)
        nfa.state_set.append(s1)
        nfa.transitions.append((s0, t, s1))
        nfa_stack.append(nfa)




def main():
    infix = input("regex: ")
    postfix = toPostfix(infix)
    print(postfix)
    allOperators = [star,line,dot]
    handler = Handler()
    nfa_stack = []
    for c in postfix:
        if c not in allOperators:
            handler.handle_char(c, nfa_stack)
        elif c == '|':
            handler.handle_alt(c, nfa_stack)
        elif c == '.':
            handler.handle_concat(c, nfa_stack)


    result = nfa_stack.pop()
    resultString = '';
    for s in result.state_set:
        resultString += s.name + ','
    resultString = resultString[:len(resultString) - 1]
    resultString += '\n'
    for a in result.alphabet:
        resultString += a + ','
    resultString = resultString[:len(resultString) - 1]
    resultString += '\n'
    resultString += result.start.name
    resultString += '\n'
    resultString += result.end.name
    resultString += '\n'
    for t in result.transitions:
        resultString += "(" + str(t[0].name) + ',' + str(t[1]) + ', ' + str(t[2].name) + ')' + ','
    resultString = resultString[:len(resultString) - 1]

    text_file = open("task_2_result.txt", "w")
    text_file.write(resultString)
    text_file.close()


if __name__ == '__main__':
    main()


