'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
generated = random.randint(0,100)
valoare = int(input("Introduceti un numar:"))
while valoare != generated:
    if valoare > generated:
        print("Caut un numar mai mic")
        valoare = int(input("Introduceti un alt numar:"))
    else:
        print("Caut un numar mai mare")
        valoare = int(input("Introduceti un alt numar:"))
print("Corect!")