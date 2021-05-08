def split(word):
    for i in word:
        my_list.append(i)

def veya(word):
   item1 = '|'
   if item1 in my_list:
       index = my_list.index(item1)
       #my_list[0] = first item
       #my_list[-1] = last item
       a = my_list[:index]
       b = my_list[(index+1):]
       print(a or b)

   else:
       print("sıctın aq nabıyon")





word = 'abb|bcd'

my_list = []

split(word)

veya(my_list)




