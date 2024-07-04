# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 17:19:27 2024

@author: Baxtiyor
"""

# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# # print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")
    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# # print(mahsulotlar.keys())

# # print('Do\'kondagi mahsulotlar:')
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())

# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# =============================================================================
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# =============================================================================
# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])
# print("Python izohli lugati: \n")
# for key, value in sorted(python_izohli_lugati.items()):
#         print(f"{key} = {value}")
# =============================================================================
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# =============================================================================

# dp = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# print("Davlatlar:")
# for k in sorted(dp.keys()):
#     print(f'{k.upper()}')
# print("\nPoytaxtlar:")
# for v in sorted(dp.values()):
#     print(f'{v.title()}')
    
# =============================================================================
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.    
# =============================================================================
# country = input("Istalgan davlatni kiriting! \n>>>").lower()
# capital = dp.get(country)
# if capital==None: print("Bizda bunday ma'lumot yo'q!")
# else: print(f"{country.upper()}ning poytaxti {capital.title()}")

# =============================================================================
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# =============================================================================
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
print("3 ta taom buyurtma bering!")
buyurtma = []
for n in range(3):
    buyurtma.append(input(f"{n+1}-chi taomni kiriting!\n>>>").lower())
for taom in buyurtma:
    if taom in menu:
        print(f"{taom.title()}ning narxi {menu[taom]} so'm.")
    else: print(f"Kechirasiz, bizda {taom.title()} yo'q.") 
     
































