
#characters
def d(str1):
    str1 = input("metin girin: ")
    numbers = []
    for i in str1.split(" "):
        if i.isdigit():
            numbers.append(i)
    print(numbers)

def D(str2):
    str2 = input("metni girin: ")
    nonDigit = []
    for i in str1.split(" "):
        if not i.isdigit():
            nonDigit.append(i)
    print(nonDigit)
def w(str3):
    str3 = input("metni girin: ")
    wordChar = []
    wordChar2 = []
    count = 0
    while count < len(str3):
        x = str3[count]
        wordChar.append(x)
        count += 1

    for i in wordChar:
        if  i.isdigit() or i.isalpha():
            wordChar2.append(i)
    print(wordChar2)

def W(str4):
    str4 = input("metni girin: ")
    nonWordChar = []
    nonWordChar2 = []
    count = 0
    while count < len(str4):
        x = str4[count]
        nonWordChar.append(x)
        count += 1
    for i in nonWordChar:
        if not i.isdigit() and not i.isalpha():
            nonWordChar2.append(i)
    print(nonWordChar2)

def s(str5):
    str5 = input("metin girin: ")
    whiteSpace = []
    for i in str5.split():
        if i == " " or i =="    ":
            whiteSpace.append(i)
    print(whiteSpace)

def S(str6):
    str6 = input("metin girin: ")
    nonWhiteSpace = []
    for i in str6.split():
        if not i == " " or not i =="    ":
            nonWhiteSpace.append(i)
    print(nonWhiteSpace)

def b(str7):
    str7 = input("metin girin: ")
    wordBoundary = []
    count = 0
    while count < len(str7):
        x = str7[count]
        wordBoundary.append(x)
        count += 1

    print(wordBoundary)

#dosya alınması


#pattern nin alınması

pattern = "bsdfjk jbr23 jwe78"
print(d(pattern))

#arama, serach()

#match