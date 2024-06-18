# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:50:03 2024

@author: Baxtiyor
"""

# =============================================================================
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing,
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing!
# =============================================================================

# ismlar = []
# ismlar.append("Kamol")
# ismlar.append("Jamol")
# ismlar.append("Shamol")
# ismlar.append("Hamol")
# for ism in ismlar:
#     print(f"Qanday ishlar", ism)
    
# =============================================================================
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan
# xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# =============================================================================
# print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

# sonlar = list(range(11, 100, 2))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")
    
# =============================================================================
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# =============================================================================
# kinolar = []
# print("5 ta eng sevimli kinolaringizni kiriting?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino: "))
# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

ismlar = []
son = int(input("Bugun nechta odam bilan uchrashdingiz yoki suhbatlashdingiz? \n>>>"))
for s in range(son):
    ismlar.append(input(f"{s+1}-odamning ismi: "))
print(ismlar)
