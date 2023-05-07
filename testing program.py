import time #importujemy bibliotekę
import random #importujemy bibliotekę
from colorama import init #importujemy podrozdział biblioteki
init()
from colorama import Fore, Back, Style #importujemy podrozdziały biblioteki
import json #importujemy bibliotekę
with open('data/qestions.json') as file: #lączymy programę z pytaniami json
    qstns = json.load(file)
random.shuffle(qstns) #przetasujemy pytania w tablicy
qstnsQty = 0 #deklarujemy zmienną, która mówi o ilości zadanych pytań
correctAns = 0 #deklarujemy zmienną, która mówi o ilości prawidłowych odpowiedzi
wrongAns = 0 #deklarujemy zmienną, która mówi o ilości nieprawidłowych odpowiedzi
counter = 0 #deklarujemy zmienną, zmienia ilość wszystkich pytań
for element in qstns:
    counter += 1
    print(Fore.YELLOW + 'Question:', element['qestion'], Style.RESET_ALL + ' ' )
    print( 'Please, choose the correct answer.')
    a = 0
    correctAnsversString = element['answers'][element['correctAnswer'] - 1]
    qstnsQty += 1
    random.shuffle(element['answers'])
    for answer in element['answers']:
        a +=  1
        print(Fore.BLUE + ' ',a, '.', Style.RESET_ALL + ' ' , answer)
    print('What answer is right?')
    userAns = ''
    while not(userAns == '1' or userAns == '2' or userAns == '3' or userAns == '4'):
        print('enter 1, 2, 3 or 4.')
        userAns = input()
    userAnsStr =  element['answers'][ int(userAns)- 1]
    if  correctAnsversString ==  userAnsStr:
        print( Fore.GREEN + 'Right!', Style.RESET_ALL + ' ')
        correctAns += 1
    else:
        print(Fore.RED + 'No.' , Style.RESET_ALL + 'the correct answer is', correctAnsversString)
        wrongAns += 1
    if counter == 30: #ustaliamy po jakiej ilości zadanych pytań pokażą się wyniki
        break
pers = (correctAns / qstnsQty) * 100  #procent poprawnych odpowiedzi  
print('quantity of answers ',qstnsQty)
print('quantity of correct answers ',correctAns)
print('quantity of wrong answers ',wrongAns)
print(pers, '%')
time.sleep(5)




        
        
