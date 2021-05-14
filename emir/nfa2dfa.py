#KTÜ project for Automata Theory.
#NFA to DFA module.
#By Emir Özmen.

class NFA:
    def __init__(self): #->Data will be taken from enfa2nfa
        #This part will be completed after re2nfa ends.
        self.state_numb = 0 #
        self.states = []
        self.symbols = [] #
        self.accepting_states_numb = 0
        self.accepting_states = [] #
        self.start_state = 0 #
        self.transition_roads = [] #

    def create_states(self):
        self.states = list(range(self.state_numb))


    def print(self): #For printing to console.
        print(self.state_numb)
        print(self.states)
        print(self.symbols)
        print(self.accepting_states_numb)
        print(self.accepting_states)
        print(self.start_state)
        print(self.transition_roads)

    def txt2nfa(self, lines): #For getting data from the .txt
        self.state_numb = int(lines[0])
        self.create_states()
        self.symbols = list(lines[1].strip())

        accepting_states_registor = lines[2].split(" ")
        for index in range(len(accepting_states_registor)):
            if index == 0:
                self.accepting_states_numb = int(accepting_states_registor[index])
            else:
                self.accepting_states.append(int(accepting_states_registor[index]))

        self.start_state = int(lines[3])

        for index in range (4, len(lines)):
            transition_road_register = lines[index].split(" ")

            state1 = int(transition_road_register[0])
            transition_symbol =transition_road_register[1]
            state2 = int(transition_road_register[2])

            transition_road = (state1, transition_symbol, state2)
            self.transition_roads.append(transition_road)

class DFA:
    def __init__(self):
        self.state_numb = 0
        self.symbols = []
        self.accepting_states_numb = 0
        self.accepting_states = []
        self.start_state = 0
        self.transition_roads = []
        self.states = [] #

    def nfa2dfa(self, nfa):
        self.symbols = nfa.symbols
        self.start_state = nfa.start_state

        nfa_transition_dict = {}
        dfa_transition_dict = {}

        #NFA geçişlerini birleştir
        for transition in nfa.transition_roads:
            state1 = transition[0]
            transition_symbol = transition[1]
            state2 = transition[2]

            if(state1, transition_symbol) in nfa_transition_dict:
                nfa_transition_dict[(state1, transition_symbol)].append(state2)
            else:
                nfa_transition_dict[(state1,transition_symbol)] = [state2]

        self.states.append((0,))

        #NFA transitions to DFA transitions
        for dfa_state in self.states:
            for symbol in nfa.symbols:
                if len(dfa_state) == 1 and (dfa_state[0],symbol) in nfa_transition_dict:
                    dfa_transition_dict[(dfa_state, symbol)] = nfa_transition_dict[(dfa_state[0], symbol)]

                    if tuple(dfa_transition_dict[(dfa_state, symbol)]) not in self.states:
                        self.states.append((tuple(dfa_transition_dict[(dfa_state, symbol)])))
                else:
                    targets = []
                    last_target = []

                    for nfa_state in dfa_state:
                        if (nfa_state, symbol) in nfa_transition_dict and nfa_transition_dict[(nfa_state, symbol)] not in targets:
                            targets.append(nfa_transition_dict[(nfa_state, symbol)])

                    if not targets:
                        last_target.append(None)
                    else:
                        for target in targets:
                            for value in target:
                                if value in last_target:
                                    last_target.append(value)

                    dfa_transition_dict[(dfa_state, symbol)] = last_target

                    if tuple(last_target) not in self.states:
                        self.states.append((tuple(last_target)))

        #Converting the states

        for key in dfa_transition_dict:
            self.transition_roads.append(((self.states.index(tuple(key[0])), key[1], self.states.index(tuple(dfa_transition_dict[key])))))

        for q_state in self.states:
            for nfa_accepting_state in nfa.accepting_states:
                if nfa_accepting_state in q_state:
                    self.accepting_states.append(self.states.index(q_state))


    def print_dfa(self):
        print(len(self.states))
        print("".join(self.symbols))
        print(str(self.accepting_states_numb) + " " + " ".join(str(accepting_state) for accepting_state in self.accepting_states))

        for transition in sorted(self.transition_roads):
            print(" ".join(str(value) for value in transition))