# een prog om de tafels te oefenen

from random import randint

import random

mylist = [1,2,3,4,5,10]
feliciaties = ["Goed Zo!!", "Doe zo verder!","Jij bent de beste!", "Correct!!", "Fantastisch!!!", "Goed bezig ;-)" ]
print(random.choice(feliciaties))
#vraag de naam van de user

name = input('Wat is je naam?: ')

print ('---'*40)
print ('Dag '+ name +', we gaan een beetje tafels oefenen.')
print ('Ik weet dat je het al goed kan, maar oefenen kan nooit kwaad.')
print ('Dikke Kussen van papa, XXX ')
print ('---'*40)

for i in range(0,50):
    x = random.choice(mylist)
    y = randint(1,9)
    print ('Hoeveel is:')
    value = eval(input(''+ str(x) + ' maal ' + str(y) + ' = '))
    if value == x*y:
        print(random.choice(feliciaties))

    else:
        while value != x*y:
            print('Foutje, probeer opnieuw')
            value = eval(input(''+ str(x) + ' maal ' + str(y) + ' = '))
