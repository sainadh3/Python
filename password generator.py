# generate a password by defining no of each type of characters required
import random

n=int(input('enter the length of password required\n'))
n1=int(input('enter the no of cap letters required\n'))
n2=int(input('enter the no of small letters required\n'))
n3=int(input('enter the no of numbers required\n'))
n4=int(input('enter the no of spl characters required\n'))
cap_l=[chr(i) for i in range(65,91)]
sma_l=[chr(i) for i in range(97,123)]
num=[chr(i) for i in range(48,58)]
# password special characters from owasp.org
spl_ch=list(''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
dic={0:cap_l,1:sma_l,2:num,3:spl_ch}
l=[n1,n2,n3,n4]
password=[]

if sum(l)==n:
    for i in range(len(l)):
        for j in range(l[i]):
            password.append(random.choice(dic[i]))

else: print('given req no of letters not equals to the length of pass')

for i in range(n):
    random.shuffle(password)
print(''.join(password))

##########################################################################################################
# generate a password of random length between 6 to 12

from random import randrange,choice,shuffle,randint

n=randint(6,12)
cap_l=[chr(i) for i in range(65,91)]
sma_l=[chr(i) for i in range(97,123)]
num=[chr(i) for i in range(48,58)]
# password special characters from owasp.org
spl_ch=list(''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
dic={0:cap_l,1:sma_l,2:num,3:spl_ch}

def randparts(number, divider, min_value, max_value):
    sum_min = divider * min_value
    if sum_min > number:
        return

    number -= sum_min
    result = [min_value] * divider
    while number:
        pocket = randrange(divider)
        if result[pocket] <= max_value:
            result[pocket] += 1
            number -= 1

    return result
l=randparts(n,4,0,9)


password=[]

for i in range(len(l)):
    for j in range(l[i]):
        password.append(choice(dic[i]))

for i in range(n):
    shuffle(password)
print(''.join(password))