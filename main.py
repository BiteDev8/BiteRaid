from colorama import Fore, Back, Style, init
import time
import random
import pyfiglet
T = "BiteRaid"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
init()

print(Fore.GREEN+"id qui faut raid")
id = int(input())
taille = random.randint(6,9)
chiffre = "0123456789"
carractere = "AZERTYUOIPMLKJHGFDSQWXCVBNnbvcxwqsdfghjklmpoiuytrea1234567890"
x=0
while True :
	x+=1
	bot = ''.join((random.choice(carractere)for i in range(int(taille))))
	tag = ''.join((random.choice(chiffre)for i in range(4)))

	print(Fore.RED+"send ==>[",x,"]",bot+"#"+tag,"ALT F4 for close")
