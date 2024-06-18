# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:06:03 2024

@author: Baxtiyor
"""

# =============================================================================
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# =============================================================================

#son = float(input('Juft son kiriting!'))
#if son 
# a = int(5)
# print(a%2, a/2)

# =============================================================================
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# =============================================================================

# yosh = int(input("Yoshingiz kiriting! \n >>>"))
# if yosh<4 or yosh>60: narh = 0
# elif 4<yosh<18: narh = 10000
# else: narh = 20000
# print(f"Siz uchun chipta narhi {narh} so'm etib belgilangan!")

# =============================================================================
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning
# teng yoki katta/kichikligi haqida xabarni chiqaring
# =============================================================================

# a = float(input("1-sonni kiriting!"))
# b = float(input("2-sonni kiriting!"))
# if a==b: print("Ushbu sonlar teng!")
# elif a>b: print(f"{a} katta {b} dan!")
# else: print(f"{a} kichik {b} dan!")

# =============================================================================
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# =============================================================================

# mahsulotlar = ['non', 'choy', 'shakar', 'yog', 'tuxum', 'un', 'sut', 'tuz', 'mosh', 'karam']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# for s in savat:
#     if s in mahsulotlar:
#         print(f"Mahsulot do'konimizda bor!")
#     else: 
#         print(f"Mahsulot do'konimizda yo'q!")
        
# =============================================================================
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, 
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa
# "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# =============================================================================
# mahsulotlar = ['non', 'choy', 'shakar', 'yog', 'tuxum', 'un', 'sut', 'tuz', 'mosh', 'karam']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# for s in savat:
#     if s in mahsulotlar:
#         bor_mahsulotlar.append(s)
#     else: 
#         mavjud_emas.append(s)
# if len(mavjud_emas)==0: print("Siz so'ragan barcha mahsulotlar do'konimizda bor!")
# else: print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")

# =============================================================================
# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda
# bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!"
# xabarini chiqaring.
# =============================================================================

# users = ["kamol", "komil", "umar", "bek", "sobir"]
# login = input("Yangi login tanlang! \n>>>")
# if login.lower() in users: 
#     print("Login band, yangi login tanlang!")
# else: 
#     print(f"Xush kelibsiz, {login.title()}!")   
    
# =============================================================================
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi 
# kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# =============================================================================

# son = int(input("Biror butun son kiriting! \n>>>"))
# b = []
# for s in range(2,11):
#     if son%s==0: b.append(s)
# print(b)    

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


































