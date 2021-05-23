import tkinter as tk
from tkinter import filedialog
from tkinter import *
from graphviz import Digraph
import re2nfa
import nfa2dfa




def tester():
    # read data from text file
    f = open("output_dfa.txt", 'r')

    symbols = f.readline().split()
    states = f.readline().split()
    start_state = f.readline().strip()
    finish_states = f.readline().split()

    # transmisions is our delta
    transmissions = {}

    def letter_counter(input):  # For counting the letters.
        dict = {}
        for l in input:
            keys = dict.keys()
            if l in keys:
                dict[l] += 1
            else:
                dict[l] = 1
        return dict

    # for reducing memory usage we use list for transmision and dicuse it in worksheet
    for x in states:
        transmissions[x] = [None] * len(symbols)

    # here we dont use while loop because we are sure that each dfa delta function for every state has vertex by number of symbols letters
    for i in range(len(symbols) * len(states)):
        trans = f.readline().split()
        alp_index = symbols.index(trans[1])
        transmissions[trans[0]][alp_index] = trans[2]
    # print(transmissions)

    f = open("strings.txt", "r")
    strings = f.read().splitlines()
    f2 = open("output.txt", "w+")
    for string in strings:
        f2.write(string)
        inputStr = string

        # here we check if input string contains some letters that we dont have them in out symbols
        # warn the user and wants input new string
        string_letters = list(letter_counter(inputStr).keys())
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
            except KeyError:  # It will keep working if 'trap' statement comes.
                continue

        # after iteration bt symbols and
        if (ps in finish_states):
            f2.write(' -> Accepted.\n ')



        else:
            f2.write(" -> Not accepted.\n")





"""Pencere özellikleri"""
pencere =tk.Tk()
pencere.title("Automata Project")
pencere.geometry('1100x760+200+30') #birincisi genişlik ikinci yükseklik 3.x konumu 4.ykonumu
pencere.config(bg='light gray')  #bg background
pencere.iconbitmap('Image//logo.ico') #pencerenin logosu



"""GENEL YAZILAR"""

ekranYazisi1=tk.Label(pencere,text='RE 2 NFA-DFA',fg='black',font='Times 15 ') #fg yazının rengi
ekranYazisi1.pack()

ekranYazisi2=tk.Label(pencere,text='Open Text File',fg='black',font='Times 10')
ekranYazisi2.place(x=120,y=50)

ekranYazisi3=tk.Label(pencere,text='Enter Regular Expression',fg='black',font='Times 10')
ekranYazisi3.place(x=120,y=142)

#KTU LOGOLARI
logosol = PhotoImage(file=r"Image//leftlogo.png") #amblemler
ekranYazisi4=tk.Label(pencere,image=logosol)
ekranYazisi4.place(x=2,y=645)

logosag=PhotoImage(file=r"Image//rightlogo.png")
ekranYazisi4=tk.Label(pencere,image=logosag)
ekranYazisi4.place(x=1012,y=645)



"""TEXT BOLUMU"""


def open_txt():
    text_file =filedialog.askopenfilename(initialdir="//Desktop",title='Open Text File',filetypes=(("Text Files","*.txt"),))
    ##bu dosyayı açma kısmı initialdirdeki kısımda açar direk ekranını,filetypesda sadece o tipleri açmasını sağlar
    text_file = open("strings.txt", 'r')
    stuff = text_file.read()

    my_text.insert(END,stuff)
    text_file.close()

def save_txt():
    text_file = open("strings.txt", 'w')
    text_file.write(my_text.get(1.0, END))

my_text =Text(pencere,width=90,height=4)
my_text.place(x=120,y=73)
6
def displayer():
    f3 = open("output.txt", "r")
    f3 = f3.read().splitlines()
    for asdas in f3:
        listBox_0.insert(END, asdas)

"""
def color():
    f5 = open("output.txt", "r")
    lines = f5.readlines()
    for line in lines:
        if ('Not' in line):
            listBox_0.config(fg='red')
            print("kırmızı")
            
            f5.close()

        else:
            listBox_0.config(fg='green')
            print("yesil")
            f5.close()
"""
def cleaner():

    listBox_0.delete(1)

"""REGEX TEXT BOLUMU"""

def regex():
    text_file = open("input.txt", 'r+')
    stuff = text_file.read()
    regex_text.insert(END, stuff)
    text_file.write(regex_text.get(1.0, END))
    text_file.close()
    re2nfa.main()
    open("input.txt", "w").close() #input'u temizlemek için.
    nfa2dfa.main()
    tester()
    #color()
    cleaner()
    displayer()




def regexClear():
    regex_text.delete(1.0,END)

regex_text=Text(pencere,fg='red',font='Times',relief=tk.FLAT,width=90,height=2)
regex_text.place(x=120,y=165)

buton4=tk.Button(text='Execute',fg='white',font='Times',bg='red',borderwidth=4,command=regex)
buton4.place(x=850,y=165)

buton5=tk.Button(text='Clear',fg='white',font='Times',bg='red',borderwidth=4,command=regexClear)
buton5.place(x=930,y=165)




"""LISTBOX SCROLLBAR VE BUTONLARI"""

my_frame = Frame(pencere) #listboxda scrollbarda frame e göre konumlanıyor daha rahat edebilmek adına framei kullanıyoruz
my_frame.place(x=550,y=300)

my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=Y)
listBox_0 = tk.Listbox(my_frame, width=85, height=20, yscrollcommand=my_scrollbar.set, selectmode='single') #single tek multiple çoklu

listBox_0.pack()

my_scrollbar.config(command=listBox_0.yview)


def backButtonFN(my_frame):
    curselection = listBox_0.curselection()
    indexLB = curselection[0]
    indexLB = indexLB - 1
    if indexLB > 0 or indexLB == 0:
        listBox_0.selection_clear(0, last='end')
        listBox_0.selection_set(indexLB)
    else:
        None
pass

def forwardButtonFN(my_frame):
    curselection = listBox_0.curselection() #current selection method
    indexLB = curselection[0] #get value of index
    indexLB = indexLB + 1 #add 1 to current value
    listBox_0.selection_clear(0, last='end') #delete old selection
    listBox_0.selection_set(indexLB) #select new index
pass

backButton = tk.Button(pencere)
backButton.configure(text='BACK',fg='white',font='Times',bg='red',borderwidth=1)
backButton.place(x=750,y=630)
backButton.bind('<1>', backButtonFN, add='' )


forwardButton = tk.Button(pencere)
forwardButton.configure(text='FORWARD',fg='white',font='Times',bg='green',borderwidth=1)
forwardButton.place(x=820,y=630)
forwardButton.bind('<1>', forwardButtonFN, add='' )



listBox_0.selection_set(0) #activate first index



"""GENEL FONKSIYONLAR"""


def tamEkran():
    pencere.state('zoomed')

def normalEkran():
    pencere.state('normal')

def cikis():
    exit()

def bBlack(): #edit kısmındaki menu arka plan rengi degistirme komutları bBlack,bRed,bOriginal,menu kısmında
    pencere.config(bg='black')

def bRed():
    pencere.config(bg='red')

def bOriginal():
    pencere.config(bg='light gray')

def transparentWindow():
    pencere.wm_attributes('-alpha',0.3)

def opaqueWindow():
    pencere.wm_attributes('-alpha',1)
def clear():
    my_text.delete(1.0,END)


"""GENEL BUTONLAR"""

buton1=tk.Button(text='Open',fg='white',font='Times',bg='red',borderwidth=4,command=open_txt) #borderwith buton genisligi
buton1.place(x=850,y=85)

buton2=tk.Button(text='Save',fg='white',font='Times',bg='red',borderwidth=4,command=save_txt)
buton2.place(x=920,y=85)

buton3=tk.Button(text='Clear',fg='white',font='Times',bg='red',borderwidth=4,command=clear) #borderwidth buton genişliği
buton3.place(x=990,y=85)




"""MENU BOLUMU"""

menubar=Menu(pencere)

file=Menu(menubar,tearoff=0)
file.add_command(label="Full Screen",command=tamEkran)
file.add_separator() #menu seçenekleri arasına çizgi koymaya yarar
file.add_command(label="Normal Screen",command=normalEkran)
file.add_separator()
file.add_command(label="Exit",command=cikis)
menubar.add_cascade(label='File',menu=file) #ismi


duzen=Menu(menubar,tearoff=0) #tearoff 1 olursa ilgili menünün üstünde kesikli çizgiler olur buna tıklarsanız menünün özelliklerini ayrı bir pencerede açar
duzen.add_command(label="Background: Black",command=bBlack)
duzen.add_separator()
duzen.add_command(label="Background: Red",command=bRed)
duzen.add_separator()
duzen.add_command(label="Background: Original",command=bOriginal)
duzen.add_separator()
duzen.add_command(label="Transparent Window",command=transparentWindow)
duzen.add_separator()
duzen.add_command(label="Opaque Window",command=opaqueWindow)
menubar.add_cascade(label='Edit',font='Times',menu=duzen) #ismi

pencere.config(menu=menubar)


"""#TOGGLE BUTON VE DURUM DİYAGRAMLARI BOLUMU """


is_nfa = True
toggleLabel = Label(pencere, text="NFA",fg="green",font=("Helvetica bold", 15))
toggleLabel.place(x=505,y=210)

def switch():

    global is_nfa
    if is_nfa:
        from graphviz import Digraph

        g = Digraph(format='png')
        g.attr(size='10')

        nfa_button.config(image=dfa)
        toggleLabel.config(text="DFA", fg="red")
        is_nfa = False
        f = open("output_re.txt", "r")
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

        g.render('graphdfa', view=False)
        f.close()

        graphPhotoDfa =PhotoImage(file=r"graphdfa.png")
        ekranYazisi5 = tk.Label(pencere, image=graphPhotoDfa)
        ekranYazisi5.place(x=100, y=250)
        ekranYazisi5.config(size=50)


    else:

        from graphviz import Digraph

        g = Digraph(format='png')
        g.attr(size='10')

        nfa_button.config(image=nfa)
        toggleLabel.config(text="NFA", fg="green")
        is_nfa = True

        f = open("output_dfa.txt", "r")
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

        g.render('graphnfa', view=False)
        f.close()

        graphPhotoNfa =PhotoImage(file=r"graphnfa.png")
        ekranYazisi6 = tk.Label(pencere,image=graphPhotoNfa)
        ekranYazisi6.place(x=230, y=250)
        ekranYazisi6.config(size=50)



nfa = PhotoImage(file=r"Image//nfa.png")
dfa = PhotoImage(file=r"Image//dfa.png")

nfa_button = Button(pencere, image=nfa, bd=0, borderwidth=1,command=switch)
nfa_button.place(x=480,y=240)




pencere.mainloop()