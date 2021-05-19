#Automata Theory project
#KTÜ

#Getting the data from .txt file.
f = open("input.txt","r")
lines = f.readlines()
symbols = lines[0].rstrip().split()
nfa_states = lines[1].rstrip().split()
nfa_startingState = lines[2].rstrip()
nfa_finalStates = lines[3].rstrip().split()
nfa_delta = []
for line in lines[4:]:
    part = line.rstrip().split()
    nfa_delta.append(part)

f.close()

#For getting the next state.
def get_nextState(current_state, movement):
    potential_states = []
    for state in nfa_delta:
        if state[0] == current_state and state[1] == movement:
            potential_states.append(state[2])
    if len(potential_states) == 0:
        return None
    else:
        return potential_states

########### Epsilon-NFA to NFA ###########

#For getting the next state with ε expression ĞĞĞ
def epsilon_closure(state):
    related_states = [state]
    history = [state]

    while len(history) != 0:
        next_states = get_nextState(history[0], 'Îµ')

        if next_states is not None:
            for state in next_states:
                if state not in related_states:
                    related_states.append(state)
                    history.append(state)
        history.pop(0)

    return related_states


#Getting the next states without lambda
def nextState_without_epsilon(current_state,movement):
    potential_states = []

    lambda_cl = epsilon_closure(current_state)
    temporary_states = []

    for state in lambda_cl:
        next_states = get_nextState(state, movement)
        if next_states is not None:
            for s in next_states:
                if s not in temporary_states:
                    temporary_states.append(s)

    for state in temporary_states:
        temporary_states = epsilon_closure(state)
        if temporary_states is not None:
            for s in temporary_states:
                if s not in potential_states:
                    potential_states.append(s)

    if len(potential_states) != 0:
        return potential_states
    else:
        return None

########### Epsilon-NFA to NFA ###########


#Assigning the old values.
dfa_startingState = epsilon_closure(nfa_startingState)
dfa_startingState.sort()

dfa_states = [dfa_startingState]
dfa_delta = []
dfa_final_states = []

#For fixing the final states.
for f in nfa_finalStates:
    if f in dfa_startingState:
        dfa_final_states.append(dfa_startingState)

re_states = [dfa_startingState]
history = [dfa_startingState]

#Main ĞĞĞ
while len(re_states) != 0 :
    #For checking all the states
    for letter in symbols:
        states = []
        for re_state in re_states[0]:
            next_states = nextState_without_epsilon(re_state,letter)
            if next_states is not None:
                for next_state in next_states:
                    if next_state not in states:
                        states.append(next_state)


        if len(states) != 0:
            dfa_delta.append([re_states[0], letter, states])
            states.sort()

            if states not in dfa_states:
                dfa_states.append(states)
                re_states.append(states)


            for f_state in nfa_finalStates:
                if (f_state in states) and (states not in dfa_final_states):
                    dfa_final_states.append(states)
        else:
            #trap state.
            dfa_delta.append([re_states[0], letter, 'trap'])
    re_states.pop(0)


########### Sending to .txt file. ###########


f = open("output.txt","w+")

for s in symbols:
    f.write(f"{s} ")
f.write('\n')

for st in dfa_states:
    f.write(f"{''.join(list(st))} ")
f.write('\n')

f.write(f"{''.join(list(dfa_startingState))}")
f.write('\n')

for fs in dfa_final_states:
    f.write(f"{''.join(list(fs))} ")
f.write('\n')

for state in dfa_delta:
    f.write(f"{''.join(list(state[0]))} {state[1]} {''.join(list(state[2]))}")
    f.write('\n')

f.write('\b')

f.close()