##Create a function that takes a string as a parameter and returns a list.
##The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def remove_vowels_sort_constants(x):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']   
    newtext = ""
    textlen = len(x)
    for i in range(textlen):
            if x[i] not in vowels: ##Så længe x's i ikke er i vowels, kører den videre.
                newtext = newtext + x[i]
    print(newtext)
    x = sorted(newtext)
    print(x)
    return x

remove_vowels_sort_constants('Gangster')

##Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
l = ['Claus', 'Ib', 'Per']
##Sort this list by using the sorted() build in function.
x = sorted(l)
##Sort the list in reversed order.
sorted(l, reverse=True)
##Sort the list on the lenght of the name.
sorted(l, key=len)
##Sort the list based on the last letter in the name.
def last_letter_in_name(x):
    return x[-1]

x = sorted(l, key=last_letter_in_name)
print(x)
##Sort the list with the names where the letter ‘a’ is in the name first.
def find_a(x):
    return

p = sorted(l, key=find_a)

print(p)
    
  
