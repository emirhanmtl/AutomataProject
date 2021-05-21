star = '*'
line = '|'
dot = '·'
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + \
    [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
    [chr(i) for i in range(ord('0'), ord('9') + 1)]


class NFA:
    def __init__(self, start, end, ):
        self.state_set = []
        self.alphabet = []

        self.start = start
        self.end = end  # start and end states
        end.is_end = True
        self.transitions = []

def Union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list

precedence = {'(': 1, '|': 2, '.': 3, '?': 4, '*': 4, '+': 4, '^': 5}
def getprecedence(c):
    if (c in precedence):
        return precedence[c]
    else:
        return 6



# infix to postfix
def toPostfix(infix):
    postfix = ''

    stack = []



    for c in infix:
        if c == '(':
            stack.append(c);
        elif c == ')':

            while (stack[len(stack) - 1] != '('):
                postfix += stack.pop()
            stack.pop();
        else:
            while (len(stack) > 0):
                peekedChar = stack.pop()
                stack.append(peekedChar)
                peekedCharPrecedence = getprecedence(peekedChar)
                currentCharPrecedence = getprecedence(c)

                if (peekedCharPrecedence >= currentCharPrecedence):

                    postfix += stack.pop()

                else:
                    break;

            stack.append(c)
    while (len(stack) > 0):
        postfix += stack.pop()
    return postfix;

class State:

    def __init__(self, name):
        self.epsilon = []  # epsilon-closure
        self.transitions = {}  # char : state
        self.name = name
        self.is_end = False

class Handler:
    def __init__(self):
        self.state_count = 0

    def create_state(self):
        self.state_count += 1
        return State('Q' + str(self.state_count))
    def handle_char(self, t, nfa_stack):
        s0 = self.create_state()
        s1 = self.create_state()
        s0.transitions[t] = s1
        nfa = NFA(s0, s1)

        nfa.state_set.append(s0)
        nfa.state_set.append(s1)
        nfa.transitions.append((s0, t, s1))
        nfa_stack.append(nfa)

    def handle_alt(self, t, nfa_stack,infix):
        n2 = nfa_stack.pop()
        n1 = nfa_stack.pop()
        s0 = self.create_state()
        s0.epsilon = [n1.start, n2.start]
        s3 = self.create_state()
        n1.end.epsilon.append(s3)
        n2.end.epsilon.append(s3)
        n1.end.is_end = False
        n2.end.is_end = False
        nfa = NFA(s0, s3)
        for i in infix:
            if i in alphabet:
                nfa.alphabet.append(i)

        nfa.state_set = Union(n1.state_set, n2.state_set)
        nfa.state_set.extend([s0, s3])
        nfa.transitions = Union(n1.transitions, n2.transitions)
        nfa.transitions.extend([(s0, 'Îµ', n1.start), (s0, 'Îµ', n2.start), (n1.end, 'Îµ', s3), (n2.end, 'Îµ', s3)])
        nfa_stack.append(nfa)
    def handle_concat(self, t, nfa_stack,infix):
        n2 = nfa_stack.pop()
        n1 = nfa_stack.pop()
        nfa = NFA(n1.start, n2.end)
        for i in infix:
            if i in alphabet:
                nfa.alphabet.append(i)

        nfa.state_set = Union(n1.state_set, n2.state_set)
        nfa.state_set.remove(n1.end)
        nfa.transitions = Union(n1.transitions, n2.transitions)
        newtransitions = []
        for t in nfa.transitions:
            if (t[2] == n1.end):
                r = (t[0], t[1], n2.start)
                t = r

            newtransitions.append(t)
        nfa.transitions = newtransitions
        nfa_stack.append(nfa)

def main():
    with open('input.txt', 'r') as file:
        infix = file.read().replace('\n', '')
    infix = infix.replace(' ', 'ε')
    postfix = toPostfix(infix)
    print(postfix)
    allOperators = [star,line,dot]
    handler = Handler()
    nfa_stack = []
    for c in postfix:
        if c not in allOperators:
            handler.handle_char(c, nfa_stack)
        elif c == line:
            handler.handle_alt(c, nfa_stack,infix)
        elif c == dot:
            handler.handle_concat(c, nfa_stack,infix)


    result = nfa_stack.pop()
    resultString = ''
    for a in result.alphabet:
        resultString += a + ' '
    resultString = resultString[:len(resultString) - 1]
    resultString += '\n'
    for s in result.state_set:
        resultString += s.name + ' '
    resultString = resultString[:len(resultString) - 1]
    resultString += '\n'
    resultString += result.start.name
    resultString += '\n'
    resultString += result.end.name
    resultString += '\n'
    for t in result.transitions:
        resultString += str(t[0].name) + ' ' + str(t[1]) + ' ' + str(t[2].name) + '\n'
    resultString = resultString[:len(resultString) - 1]

    text_file = open('nfa_output.txt', 'w')
    text_file.write(resultString)
    text_file.close()


if __name__ == '__main__':
    main()
