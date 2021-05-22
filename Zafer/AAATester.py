import random

f = open("output.txt", 'r')
symbols = f.readline().split()
states = f.readline().split()
start_state = f.readline().strip()
finish_states = f.readline().split()

transmissions = {}


def letter_counter(input):
    dict = {}
    for L in input:
        keys = dict.keys()
        if L in keys:
            dict[L] += 1
        else:
            dict[L] = 1
    return dict


def main():

    for x in states:
        transmissions[x] = [None] * len(symbols)

    for i in range(len(symbols) * len(states)):
        trans = f.readline().split()
        alp_index = symbols.index(trans[1])
        transmissions[trans[0]][alp_index] = trans[2]
    z = 1
    while z < 11:
        z += 1
        input()
        # input_str = input()
        # if input_str == "exit":
        #    break
        deck = list(symbols)
        length = ['1', '2', '3', '4', '5', '6', '7', '8']
        y = ''.join(random.choices(length))
        y = int(y)
        result = ''.join(random.choices(deck, k=y))
        ps = start_state
        for char in result:
            try:
                ps = transmissions[ps][symbols.index(char)]
            except KeyError:
                continue

        if ps in finish_states:
            print('\033[92m', result)
        else:
            print('\033[91m', result)
        text = open("Text.txt", "w")
        text.write(result)
        text.write("\n")
        text.close()


main()
# file = open("Text.txt", "r+")
# file. truncate(0)
# file. close()
