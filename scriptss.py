from re import S


print('Hello world')

s = 4

if s > 5:
    print('dank')
elif s == 5:
    print('sjovt')
elif s < 5:
    print('hello')

def myFunction(fname):
    print('hi ' + fname)

myFunction('Silas')

def function(*kids):
    print('The second child is: ' + kids[2-1])

function("Emil", "Silas", "Guobin")