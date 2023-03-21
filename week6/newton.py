#newton method

#sqr = int(input("Enter x: "))
#ans = (x+n/x)/2
#print (f"wynik to {ans}")

#def add(x, y):
    #return x + y

#result = add(3, 5)
#print(result)    

import math


def root(number, number1):
    return number/number1

number = float(input("dawaj nr "))
number1 = math.sqrt(number)
result = root(number, number1)
print(result)
