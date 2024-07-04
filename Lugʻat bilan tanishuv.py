# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:37:58 2024

@author: Baxtiyor
"""

# =============================================================================
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson 
# haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: 
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# =============================================================================

# otam = {"ismi":"Komil", "t_yili":1961, "t_shahri":"Navoiy"}
# #print(otam['ismi'])
# print(f"Otamning ismi {otam['ismi']}, {otam['t_yili']}-yilda, {otam['t_shahri']} shahrida tug'ilgan.")

# =============================================================================
# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# =============================================================================

# taomlar = {
#     'otam':'osh',
#     'onam':'manti',
#     'ukam':'shashlik',
#     'akam':'suv',
#     'opam':'mosh'}
# print(f"Otamninig sevimli taomi {taomlar['otam']}, onamniki esa {taomlar['onam']} hamda ukamniki {taomlar['ukam']}!!!")

# =============================================================================
# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# =============================================================================

# pil = {
#        'variable':'o\'zgaruvchi',
#        'konstanta':'o\'zgarmas',
#        'string':'matn',
#        'integers':'butun_sonlar',
#        'floats':'o\'nlik_sonlar',
#        'list':'ro\'yxat',
#        'tuples':'o\'zgarmas ro\'yxat',
#        'dictionary':'lug\'at',
#        'boolean':'mantiqiy',
#        'for':'учун'}
# =============================================================================
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# =============================================================================
# kword = input("Python bo'yicha biror atama kiriting va tarjimasini bilib oling! \n>>> ")
# if kword.lower() in pil:
#     print(pil[kword.lower()])
# else: print("Bunday so'z mavjud emas")
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))