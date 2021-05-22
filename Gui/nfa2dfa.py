"""Emir Özmen"""

def main():
    # .txt dosyasından veriler alınıyor.
    f = open("output_re.txt","r")
    lines = f.readlines()
    symbols = lines[0].rstrip().split()
    nfa_states = lines[1].rstrip().split()
    nfa_startingState = lines[2].rstrip()
    nfa_finalStates = lines[3].rstrip().split()
    nfa_transitions = []
    for line in lines[4:]:
        part = line.rstrip().split()
        nfa_transitions.append(part)

    f.close()

    #Mevzubahis state'in sonraki statelerini alabilmek için.
    def get_nextState(current_state, movement):
        potential_states = []
        for state in nfa_transitions:
            if state[0] == current_state and state[1] == movement:
                potential_states.append(state[2])
        if len(potential_states) == 0:
            return None
        else:
            return potential_states

    ########### Epsilon-NFA to NFA ###########

    #Epsilon ile ilişkisi bulunan stateleri almak için.
    def related_epsilon(state):
        related_states = [state]
        registor = [state]

        while len(registor) != 0:
            next_states = get_nextState(registor[0], 'Îµ')
            if next_states is not None:
                for state in next_states:
                    if state not in related_states:
                        related_states.append(state)
                        registor.append(state)
            registor.pop(0)

        return related_states


    #Epsilon ile ilişkisi bulunmayan state'leri almak için.
    def nextState_without_epsilon(current_state,movement):
        potential_states = []

        rltd_epsilon = related_epsilon(current_state)
        temporary_states = []

        #küme içindeki herşeyin next state'ini bulmak için.
        for state in rltd_epsilon:
            next_states = get_nextState(state, movement)
            if next_states is not None:
                for s in next_states:
                    if s not in temporary_states:
                        temporary_states.append(s)


        for state in temporary_states:
            temporary_states = related_epsilon(state)
            if temporary_states is not None:
                for s in temporary_states:
                    if s not in potential_states:
                        potential_states.append(s)

        #potansiyel state olup olmadığını kontrol etmek için.
        if len(potential_states) != 0:
            return potential_states
        else:
            return None

    ########### Epsilon-NFA to NFA ###########


    #DFA verilerini yerleştirme.
    dfa_startingState = related_epsilon(nfa_startingState)
    dfa_startingState.sort()

    dfa_states = [dfa_startingState]
    dfa_transitions = []
    dfa_final_states = []

    #Aynı zamanda hem start state hem accept state olanların kontrolü. Eğer öyle ise start'ı, accept state'e ekliyoruz.
    for f in nfa_finalStates:
        if f in dfa_startingState:
            dfa_final_states.append(dfa_startingState)

    remaining_states = [dfa_startingState]
    registor = [dfa_startingState]

    #elimizdekiler bitene kadar döngüye devam.
    while len(remaining_states) != 0 :
        #Teker teker tüm stateleri kontrol edip transitionları ve next stateleri düzenliyoruz.
        for letter in symbols:
            states = []
            for remaining_state in remaining_states[0]:
                #harf ile gelen bütün next state'leri bulmak için.
                next_states = nextState_without_epsilon(remaining_state,letter)
                if next_states is not None:
                    for next_state in next_states:
                        if next_state not in states:
                            states.append(next_state)

            #sonraki statelerin eklenmesi.
            if len(states) != 0:
                dfa_transitions.append([remaining_states[0], letter, states])
                states.sort()

                #statelerde tekrar olup olmadığı..
                if states not in dfa_states:
                    dfa_states.append(states)
                    remaining_states.append(states)

                #final states düzenlemesi.
                for f_state in nfa_finalStates:
                    if (f_state in states) and (states not in dfa_final_states):
                        dfa_final_states.append(states)
            else:
                #trap state. eğer next state yok ise buraya yönlendirilecek.
                dfa_transitions.append([remaining_states[0], letter, 'trap'])
        remaining_states.pop(0)


    ########### text dosyasına yollama kısmı. ###########


    f = open("output_dfa.txt","w+")

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

    for state in dfa_transitions:
        f.write(f"{''.join(list(state[0]))} {state[1]} {''.join(list(state[2]))}")
        f.write('\n')

    print("done")
if __name__ == '__main__':
    main()