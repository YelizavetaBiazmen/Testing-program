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
currentMaxQtyQstns = 30 #maksymalna ilość pytań
qstnsQty = 0 #ilość zadanych pytań
correctAns = 0 #ilość prawidłowych odpowiedzi
wrongAns = 0 #ilość nieprawidłowych odpowiedzi
counter = 0 #zawiera liczbę już zadanych pytań

#cykl dla zadawania pytań
for element in qstns:
    counter += 1 
    print(Fore.YELLOW + 'Question:', element['qestion'], Style.RESET_ALL + ' ' ) 
    print( 'Please, choose the correct answer.')
    numberOfAns = 0 #deklarujemy zmienną, która numeruje odpowiedzi
    
    #odzyskujemy i wpisujemy do zmiennej poprawną odpowiedz z tablicy, odejmując 1, ponieważ numeracja w tablicy zaczyna się od 0
    correctAnsversString = element['answers'][element['correctAnswer'] - 1] 
    random.shuffle(element['answers']) #przetasujemy odpowiedzi w tablicy
    
    #cykl dla odwowiedzi
    for answer in element['answers']:
        numberOfAns +=  1
        print(Fore.BLUE + ' ',numberOfAns, '.', Style.RESET_ALL + ' ' , answer) 
    print('What answer is right?') 
    userAns = '' #deklarujemy zmienną, do której potem wpiszemy odpowiedz użytkownika
    
    #czekamy aż użytkownik napisze jedną z możliwych odpowiedzi
    while not(userAns == '1' or userAns == '2' or userAns == '3' or userAns == '4'): 
        print('enter 1, 2, 3 or 4.')
        userAns = input() #przenosimy odpowiedz do zmiennej
    userAnsStr =  element['answers'][ int(userAns)- 1]
    if  correctAnsversString ==  userAnsStr: #sprawdzamy, czy jest odpowiedz poprawna 
        print( Fore.GREEN + 'Right!', Style.RESET_ALL + ' ') 
        correctAns += 1 #dodajemy poprawną odpowiedz
    else:
        print(Fore.RED + 'No.' , Style.RESET_ALL + 'the correct answer is', correctAnsversString) 
        wrongAns += 1 #dodajemy niepoprawną odpowiedz
    if counter == currentMaxQtyQstns: #ustaliamy po jakiej ilości zadanych pytań pokażą się wyniki
        break
pers = (correctAns / qstnsQty) * 100  #procent poprawnych odpowiedzi  
print('quantity of answers ',qstnsQty)
print('quantity of correct answers ',correctAns)
print('quantity of wrong answers ',wrongAns)
print(pers, '%')
time.sleep(5)




        
        
