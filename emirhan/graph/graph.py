from graphviz import Digraph

g = Digraph(format='png')
g.attr(size='100')
x = input("NFA mı DFA mı: ")
if (x == 'NFA'):
    f = open("output_re.txt", "r")

elif (x == 'DFA'):
    f = open("output.txt", "r")
else:
    print("Hatalı Giriş!")

lines = f.readlines()
symbols = lines[0].rstrip().split()
nfa_states = lines[1].rstrip().split()
nfa_startingState = lines[2].rstrip()
nfa_finalStates = lines[3].rstrip().split()

for line in lines[4:]:
    part = line.rstrip().split()

    if (part[1] == '1'):
        g.edge(part[0], part[2], label='1')

    elif (part[1] == '0'):
        g.edge(part[0], part[2], label='0')

    elif (part[1] == 'ε'):
        g.edge(part[0], part[2], label='ε')

    else:
        g.edge(part[0], part[2], label=part[1])

for i in nfa_states:
    if (i == nfa_states[-1]):
        g.node(i, i, shape='doublecircle')

    else:
        g.node(i, i, shape='circle')

g.render('graph', view = False)
f.close()
