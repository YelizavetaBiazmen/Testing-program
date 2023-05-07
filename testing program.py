import time #importujemy bibliotekę
import random #importujemy bibliotekę
from colorama import init #importujemy podrozdział biblioteki
init()
from colorama import Fore, Back, Style #importujemy podrozdziały biblioteki
import json #importujemy bibliotekę
with open('data/qestions.json') as file: #lączymy programę z pytaniami json
    qstns = json.load(file)
random.shuffle(qstns) #przetasujemy pytania w tablicy
#deklarujemy zmienne
qstnsQty = 0 #mówi o ilości zadanych pytań
correctAns = 0 #mówi o ilości prawidłowych odpowiedzi
wrongAns = 0 #mówi o ilości nieprawidłowych odpowiedzi
counter = 0 #zmienia ilość wszystkich pytań
for element in qstns:
    counter += 1 
    print(Fore.YELLOW + 'Question:', element['qestion'], Style.RESET_ALL + ' ' ) #kolorujemy tekst
    print( 'Please, choose the correct answer.')
    a = 0
    correctAnsversString = element['answers'][element['correctAnswer'] - 1] #odzyskujemy i wpisujemy do zmiennej poprawną odpowiedz z tablicy, odejmując 1, ponieważ numeracja w tablicy zaczyna się od 0
    qstnsQty += 1 #dodajemy pytanie 
    random.shuffle(element['answers']) #przetasujemy odpowiedzi w tablicy
    for answer in element['answers']:
        a +=  1
        print(Fore.BLUE + ' ',a, '.', Style.RESET_ALL + ' ' , answer) #kolorujemy tekst
    print('What answer is right?') 
    userAns = '' #deklarujemy zmienną, do której potem wpiszemy odpowiedz użytkownika
    while not(userAns == '1' or userAns == '2' or userAns == '3' or userAns == '4'): #zmuszamy napisać 1, 2, 3 czy 4
        print('enter 1, 2, 3 or 4.')
        userAns = input() #przenosimy odpowiedz do zmiennej
    userAnsStr =  element['answers'][ int(userAns)- 1]
    if  correctAnsversString ==  userAnsStr: #sprawdzamy, czy jest odpowiedz poprawna 
        print( Fore.GREEN + 'Right!', Style.RESET_ALL + ' ') #kolorujemy tekst
        correctAns += 1 #dodajemy poprawną odpowiedz
    else:
        print(Fore.RED + 'No.' , Style.RESET_ALL + 'the correct answer is', correctAnsversString) #kolorujemy tekst
        wrongAns += 1 #dodajemy niepoprawną odpowiedz
    if counter == 30: #ustaliamy po jakiej ilości zadanych pytań pokażą się wyniki
        break
pers = (correctAns / qstnsQty) * 100  #procent poprawnych odpowiedzi  
print('quantity of answers ',qstnsQty)
print('quantity of correct answers ',correctAns)
print('quantity of wrong answers ',wrongAns)
print(pers, '%')
time.sleep(5)




        
        
