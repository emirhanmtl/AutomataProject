from collections import Counter

# read data from text file
f = open("output.txt", 'r')
symbols = f.readline().split()
states = f.readline().split()
start_state = f.readline().strip()
finish_states = f.readline().split()
# transmisions is our delta
transmissions = {}

# for reducing memory usage we use list for transmision and dicuse it in worksheet
for x in states:
    transmissions[x] = [None] * len(symbols)

# here we dont use while loop because we are sure that each dfa delta function for every state has vertex by number of symbols letters
for i in range(len(symbols) * len(states)):
    trans = f.readline().split()
    alp_index = symbols.index(trans[1])
    transmissions[trans[0]][alp_index] = trans[2]
# print(transmissions)


while (True):
    inputStr = input("input your string : ")
    if inputStr == "exit":
        break

    # here we check if input string contains some letters that we dont have them in out symbols
    # warn the user and wants input new string
    string_letters = list(Counter(inputStr).keys())
    if set(string_letters) - set(symbols) == set():
        pass
    else:
        print("your string contains some letters that is not in your dfa symbols")
        print("try again")
        continue

    # ps is stand for present state
    ps = start_state
    for char in inputStr:
        try:
            ps = transmissions[ps][symbols.index(char)]
        except KeyError: #It will keep working if 'trap' statement comes.
            continue


    # after iteration bt symbols and
    if (ps in finish_states):
        print("String is accepted.")
    else:
        print("string is not accepted")
