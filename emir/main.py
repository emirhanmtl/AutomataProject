from nfa2dfa import NFA, DFA


filename = input("Enter the name of the TXT: ")

file = open(filename, "r")
lines = file.readlines()
file.close()

nfa = NFA()
dfa = DFA()

nfa.txt2nfa(lines)
dfa.nfa2dfa(nfa)

dfa.print_dfa()