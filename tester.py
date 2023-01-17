from gtts import gTTS
import os
import time
import random
import pygame 
from colorama import init
init()
pygame.init()
from colorama import Fore, Back, Style
import json
with open('data/qestions.json') as file:
    qstns = json.load(file)
random.shuffle(qstns)
qstnsQty = 0
correctAns = 0
wrongAns = 0 
counter = 0
for element in qstns:
    tts = gTTS(text=element['qestion'], lang='en')
    tts.save("./good.mp3")
    pygame.mixer.music.load("./good.mp3")
    pygame.mixer.music.play()
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
    if counter == 30:
        break
pers = (correctAns / qstnsQty) * 100    
print('quantity of answers ',qstnsQty)
print('quantity of correct answers ',correctAns)
print('quantity of wrong answers ',wrongAns)
print(pers, '%')
time.sleep(5)




        
        
