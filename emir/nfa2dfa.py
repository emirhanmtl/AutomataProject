# getting the conditions from the text file.
f = open("NFA_input.txt", "r")
lines = []
while True:
    line = f.readline()
    if line == '':
        break
    lines.append(line)

symbols = lines[0].split()
states = lines[1].split()
startState = lines[2].split()
acceptStates = lines[3].split()
transitions = []
for i in range(4, len(lines)):
    x = lines[i].split()
    transitions.append(x)


# Translating Epsilon-NFA to NFA
for state in reversed(transitions):
    if state[1] == 'β':
        for i in transitions:
            if i[0] == state[2]:
                temp = [state[0], i[1], i[2]]
                transitions.append(temp)
                if startState.count(state[0]) > 0 and startState.count(state[2]) == 0:
                    startState.append(state[2])
                if acceptStates.count(state[2]) > 0 and acceptStates.count(state[0]) == 0:
                    acceptStates.append(state[0])
        transitions.remove(state)
print("the nfa without lambda moves:")
print(*transitions)
print("nfa's final states:")
print(*acceptStates)
print("nfa's initial states:")
print(*startState)

#For transfering the data from string, to list
def string2list(l):
    return [(l[i: i + 2]) for i in range(0, len(l), 2)]


def nextState(current, c):  #ĞĞĞ
    l = []
    for i in transitions:
        if i[0] == current and i[1] == c:
            l.append(i)
    tmp = ""
    for j in l:
        tmp += j[2]
    return [current, c, tmp]

#For creating next states for DFA, and deleting the duplicate ones.
def func(list):
    temp = []
    for a in list:
        h = string2list(a)
        for t in h:
            if temp.count(t) == 0:
                temp.append(t)
    tmp = ''.join(map(str, temp))
    return tmp


dfaStates = []
dfaStates.append(states[0])
dfaTransitions = []
for s in dfaStates:
    h = string2list(s) #ĞĞĞ
    print("s: ",s)
    print("h: ",h)
    for k in symbols:  #Producing states for the DFA
        li = []
        stro = []
        for c in h:
            li.append(nextState(c, k))
            stro.append(nextState(c, k)[2])

        w = func(stro)
        # print(w + " the func result")
        if dfaStates.count(w) == 0:  # adding them to dfa states
            dfaStates.append(w)
        for x in li:
            x[0] = s
            x[2] = w
            if dfaTransitions.count(x) == 0:
                dfaTransitions.append(x)


dfa = []
for a in dfaTransitions:  # checking for the duplicate lines nad removing them
    h = string2list(a[0])
    h2 = string2list(a[2])
    r = set(h)
    r1 = set(h2)
    a[0] = r
    a[2] = r1
    dfa.append(a)

# for a in dfa:
#     print(*a)
print()
dfa_f = []
f1 = open("DFA_Output_2.txt", "w")
f1.write(' '.join(map(str, symbols)))  # writing in the file
f1.write("\n")
f1.write(' '.join(map(str, dfaStates)))
f1.write("\n")
f1.write(''.join(map(str, startState[0])))
f1.write("\n")
final = []
for i in dfaStates:  # handling the the duplicates in the states of dfa and writing them in the file
    for j in acceptStates:
        if i.find(j) > -1 and final.count(i) == 0:
            tmp = set(string2list(i))
            final.append(tmp)
# print("the states:")
# print(final)
last = []
for a in final:
    if last.count(a) == 0 :
        last.append(a)
        b = ''.join(map(str, list(a)))
        f1.write(b + " ")
f1.write("\n")

for a in dfa:  # writing the transitions in the file
    if dfa_f.count(a) == 0:
        dfa_f.append(a)
        b1 = ''.join(map(str, list(a[0])))
        b2 = ''.join(map(str, list(a[2])))
        # a = ' '.join(map(str, list(a)))
        b = b1 + " " + a[1] + " " + b2
        f1.write(b + "\n")
        print(b)
f.close()
f1.close()