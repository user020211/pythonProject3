# This is a sample Python script.
import random
import math


def dano(cifr, sim, prop, kol, dlin):
    for _ in range(kol):
        s1 = random.sample([chr(i) for i in range(48, 58)], math.ceil(cifr * dlin / 100))
        a = dlin - math.ceil(cifr * dlin / 100)
        s2 = random.sample([chr(i) for i in range(33, 39)], math.ceil(sim * dlin / 100))
        b = a - math.ceil(sim * dlin / 100)
        s3 = random.sample([chr(i) for i in range(65, 94)], math.ceil(prop * dlin / 100))
        c = b - math.ceil(prop * dlin / 100)
        s4 = random.sample([chr(i) for i in range(97, 123)], c)
        s5 = (s1 + s2 + s3 + s4)
        random.shuffle(s5)
        print(*s5, sep='')
        s1.clear(), s2.clear(), s3.clear(), s4.clear(), s5.clear()


s = input('По Вашей заявке будут сгенерированы пароли, укажите количество и длину в формате x.y: ').split('.')
kol = int(s[0])
dlin = int(s[1])
cifr = int(input('Нужны ли цифры Y или N: '))
sim = int(input('Нужны ли символы Y или N: '))
prop = int(input('Нужны ли Прописные буквы Y или N: '))
dano(cifr, sim, prop, kol, dlin)


