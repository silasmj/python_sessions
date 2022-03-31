list = [1, 2, 3, 'Hello World', len, [3, 4, 5], lambda x : x+x] #Der kan være alle typer i en liste.
print(list)
print(list[-1]) # Får sidste parameter i vores liste.
print(list[-2]) # Tagen anden bagerst - '-' betyder at man tager bagfra.
print(list[2:4]) # tager fra plads 2 til 4, men ikke inkludere plads 4.

l = ['Tove', 'Hans', 'Bolette', 'Hannah', 'Silas']

def last_letter_in_name(x):
    return x[-1]

x = sorted(l, key=last_letter_in_name)
print(x)

print(l)
l.sort()
print(l)

f = open('text.txt', 'r+')
print(f.read())
##f.write('Hello world')

##open('test.txt', 'w') ##Vil oprette en ny fil kaldt test.txt. - 'w' står for hvad vi ønsker at kunne.
## w=Write, r=Read a=Append r+=read og append w+=write og read




