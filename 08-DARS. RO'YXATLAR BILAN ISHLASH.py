# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:24:21 2024

@author: Baxtiyor
"""

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# print(sorted(mehmonlar, reverse=True))

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
# print(sorted(ages))

# fruits = ['pear','banana','apple','watermelon','lemon']
# print(fruits)
# fruits.reverse()
# print(fruits)

# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# sonlar = list(range(0,10)) # 
# print(sonlar)

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars) 
# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'

# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)


# =============================================================================
#                              AMALIYOT
# =============================================================================

#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ['Ispaniya', 'Germaniya', 'Portugaliya', 'Fransiya']
# print(davlatlar)
# Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))
# #sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))
# Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)
# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)

# fruits = ['pear','banana','apple','watermelon','lemon']
# print(fruits)
# fruits.reverse()
# print(fruits)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, 
# keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)
#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# a = list(range(120, 1200, 2))
# #print(a)
# print('jami: ', len(a))
# #Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print("Ro'yxatdagi sonlar yig'indisi: <<<", sum(a), ">>>")

# #Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print("eng katta:", max(a), '\neng kichik', min(a), '\n \t\tularning ayirmasi:', max(a)-min(a))

# #Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print((a)[:21])
# print((a)[260:281])
# print((a)[520:])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'kabob', 'shashlik', 'tabaka', 'manti']
nonushta = taomlar[:]
del nonushta[0]
del nonushta[2]
nonushta.append('bulka')
nonushta.append('shakar')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(' Bu taomlar ro\'yhati: ', taomlar, '\n Bu esa nonushta ro\'yhati', nonushta)
nonushta[0] = "qaymoq  va non"
nonushta = tuple(nonushta)
print(taomlar[0].upper())
sorted()
for 