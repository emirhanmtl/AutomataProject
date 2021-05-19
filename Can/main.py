import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
from tkinter import *


#pencere özellikleri
pencere =tk.Tk()
pencere.title("Automata Project")
pencere.geometry('1100x760+200+30') #birincisi genişlik ikinci yükseklik 3.x konumu 4.ykonumu
pencere.config(bg='light gray')  #bg background
pencere.iconbitmap('C://Users//suley//Desktop//logo.ico') #pencerenin logosu




#GENEL YAZILAR

ekranYazisi1=tk.Label(pencere,text='RE 2 NFA-DFA',fg='black',font='Times 15 ') #fg yazının rengi
ekranYazisi1.pack()

ekranYazisi2=tk.Label(pencere,text='Open Text File',fg='black',font='Times 10')
ekranYazisi2.place(x=120,y=50)

ekranYazisi3=tk.Label(pencere,text='Enter Test XxXx',fg='black',font='Times 10')
ekranYazisi3.place(x=120,y=142)

#KTU LOGOLARI
logosol = PhotoImage(file=r"C://Users//suley//Desktop//leftlogo.png") #amblemler
ekranYazisi4=tk.Label(pencere,image=logosol)
ekranYazisi4.place(x=2,y=645)

logosag=PhotoImage(file=r"C://Users//suley//Desktop//rightlogo.png")
ekranYazisi4=tk.Label(pencere,image=logosag)
ekranYazisi4.place(x=1012,y=645)

#GIRDILER

"""girdi1=tk.Entry(pencere,fg='red',font='Times',bd=10,width=70,relief=tk.GROOVE,cursor="arrow") #relief methodu arka kabartması
girdi1.place(x=120,y=90)
"""

girdi=tk.Entry(pencere,fg='red',font='Times',bd=10,width=70,relief=tk.GROOVE,cursor="arrow")#cursor imlecin sembolü
girdi.place(x=120,y=165)

#TEXT BOLUMU
def open_txt():
    text_file =filedialog.askopenfilename(initialdir="C://Users//suley//Desktop",title='Open Text File',filetypes=(("Text Files","*.txt"),))
    ##bu dosyayı açma kısmı initialdirdeki kısımda açar direk ekranını,filetypesda sadece o tipleri açmasını sağlar
    text_file = open("C://Users//suley//Desktop//deneme.txt",'r')
    stuff = text_file.read()

    my_text.insert(END,stuff)
    text_file.close()

def save_txt():
    text_file = open("C://Users//suley//Desktop//deneme.txt", 'w')
    text_file.write(my_text.get(1.0,END))

my_text =Text(pencere,width=90,height=4,relief=tk.SUNKEN)
my_text.place(x=120,y=73)




#LISTBOX SCROLLBAR VE BUTONLARI

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
backButton.place(x=430,y=630)
backButton.bind('<1>', backButtonFN, add='' )


forwardButton = tk.Button(pencere)
forwardButton.configure(text='FORWARD',fg='white',font='Times',bg='green',borderwidth=1)
forwardButton.place(x=520,y=630)
forwardButton.bind('<1>', forwardButtonFN, add='' )

for i in range(50):
    listBox_0.insert(END, str(i)+".index")

listBox_0.selection_set(0) #activate first index



#GENEL FONKSIYONLAR


def fulEkran():
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


#GENEL BUTONLAR

buton1=tk.Button(text='Open',fg='white',font='Times',bg='red',borderwidth=4,command=open_txt) #borderwith buton genisligi
buton1.place(x=850,y=85)

buton2=tk.Button(text='Save',fg='white',font='Times',bg='red',borderwidth=4,command=save_txt)
buton2.place(x=920,y=85)

buton3=tk.Button(text='Clear',fg='white',font='Times',bg='red',borderwidth=4,command=clear) #borderwidth buton genişliği
buton3.place(x=990,y=85)

buton4=tk.Button(text='Execute',fg='white',font='Times',bg='red',borderwidth=4)
buton4.place(x=850,y=160)



#MENU BOLUMU

menubar=Menu(pencere)

file=Menu(menubar,tearoff=0)
file.add_command(label="Full Screen",command=fulEkran)
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


#TOGGLE BUTON BOLUMU

is_nfa = True
toggleLabel = Label(pencere, text="NFA",fg="green",font=("Helvetica bold", 15))
toggleLabel.place(x=505,y=210)

def switch():
    global is_nfa

    # Determin is on or off
    if is_nfa:
        nfa_button.config(image=dfa)
        toggleLabel.config(text="DFA", fg="red")
        is_nfa = False
    else:

        nfa_button.config(image=nfa)
        toggleLabel.config(text="NFA", fg="green")
        is_nfa = True

nfa = PhotoImage(file=r"C://Users//suley//Desktop//nfa.png")
dfa = PhotoImage(file=r"C://Users//suley//Desktop//dfa.png")

nfa_button = Button(pencere, image=nfa, bd=0, borderwidth=1,command=switch)
nfa_button.place(x=480,y=240)


#Graph denemeleri

is_graph_nfa = True

# Define our switch function
def switch():
    global is_graph_nfa

    # Determin is on or off
    if is_graph_nfa:
        graph_nfa_button.config(image=graphDfa)
        is_graph_nfa = False
    else:

       graph_nfa_button.config(image=graphNfa)
       is_graph_nfa= True


# Define Our Images
graphNfa = PhotoImage(file=r"C://Users//suley//Desktop//graphNFA.png")
graphDfa = PhotoImage(file=r"C://Users//suley//Desktop//graphDFA.png")

# Create A Button
graph_nfa_button = Button(pencere, image=graphNfa, bd=0, borderwidth=3,command=switch)
graph_nfa_button.place(x=50,y=400)




pencere.mainloop()

