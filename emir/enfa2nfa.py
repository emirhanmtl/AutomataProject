global nfa
nfa = parser.parse_fa()
closures = parser.parse_closures()
# TODO: implement this

print(",".join(nfa['states']))
print(",".join(nfa['alphabet']))
print(nfa['start'])
print(",".join(nfa['final']))

global dfa
dfa = {}
dfa['delta'] = []
dfa['final'] = nfa['final']

start = nfa['start']
start_e = closures[start]

begin = nfa['start']
alpha = nfa['alphabet']
delta = nfa['delta']
final = nfa['final']


# seach all relations can arrive from a ,and m  is means the intermediate variable
# it means if a->b and b->c, then we van get a->c
def search(a, m, delta, closures):
    for re in closures[a]:
        for relation in delta:
            s, c, t = relation
            if re == s:
                if ((a, c, t)) not in h:
                    h.append((a, c, t))


global h
# get others delta by adding a search function
for relation in delta:
    s, c, t = relation
    if c:
        dfa['delta'].append((s, c, t))

h = dfa['delta']

for a in nfa['states']:
    search(a, a, dfa['delta'], closures)

for a in nfa['states']:
    for re in h:
        s, c, t = re
        if s == a:
            print("{},{},{}".format(s, c, t))

print("end")