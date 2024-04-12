import time
from colorama import *

pInput=input()
p = int(pInput)

x=1
while p>=0:
    p+=1
    int = y=x+x
    print(Fore.BLUE + str(p), Fore.WHITE + str(y), "\n")
    x=y
    time.sleep(0.0001)