# This is a sample Python script.
from random import*
from math import*
s=input('По Вашей заявке будут сгенерированы пароли, укажите количество и длину в формате x.y: ').split('.')
kol=int(s[0])
dlin=int(s[1])
cifr=int(input('Нужны ли цифры Y или N: '))
s1=sample([chr(i) for i in range(48, 58)], ceil(cifr*dlin/100))
dlin-=ceil(cifr*dlin/100)
sim=int(input('Нужны ли символы Y или N: '))
s2=sample([chr(i) for i in range(33, 39)], ceil(sim*dlin/100))
dlin-=ceil(sim*dlin/100)
prop=int(input('Нужны ли Прописные буквы Y или N: '))
s3=sample([chr(i) for i in range(65, 94)], ceil(prop*dlin/100))
dlin-=ceil(prop*dlin/100)
#if input('Нужны ли строчные буквы Y или N: ') =='Y':
s4=sample([chr(i) for i in range(97, 123)], dlin)
s5=(s1+s2+s3+s4)
for i in range(kol):
    shuffle(s5)
    print(*s5, sep='')
