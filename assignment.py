#1
from calendar import month
from hashlib import new


boardOfDirectos = {"Benny", "Hans", "Tine", "Mille", "Torben", "Troels", "Søren"}
management = {"Tine", "Trunte", "Rane"}
employees = {"Niels", "Anna", "Tine", "Ole", "Trunte", "Bent", "Rane", "Allan", "Stine", "Claus", "James", "Lars"}

#who in the board of directors is not an employee?
#Benny, Hans, Mille, Torben, Troels, Søren

#who in the board of directors is also an employee?
#Tine

#how many of the management is also member of the board?
#1

#All members of the managent also an employee
#Yes

#All members of the management also in the board?
#No

#Who is an employee, member of the management, and a member of the board?
#Tine

#Who of the employee is neither a memeber or the board or management?
#Niels, Anna, Ole, Bent, Allan, Stine, Claus, James, Lars

#2
tuples = [('a', 'Alpha'), ('b', 'Beta'), ('g', 'Gamma')]
print(tuples)

#3
a = {'a', 'e', 'i', 'o', 'u', 'y'}

b = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Union
union =  a.union(b)

print(union)

# Symmetric difference

print(a ^ b)

# Difference

print(a.difference(b))

# Disjoint
disjoint =  a.isdisjoint(b)
print(disjoint)

#4
monthDict = {'JAN': 1, 
            'FEB': 2, 
            'MAR': 3, 
            'APR': 4, 
            'MAY': 5, 
            'JUN': 6, 
            'JUL': 7, 
            'AUG': 8, 
            'SEP': 9, 
            'OCT': 10, 
            'NOV': 11, 
            'DEC': 12}

def getMonth(date):
    newVar = date.split('-')
    newVar.reverse()

    xx = '20' + newVar[0], monthDict[newVar[1]], newVar[2]
    print(xx)


getMonth('8-DEC-95')