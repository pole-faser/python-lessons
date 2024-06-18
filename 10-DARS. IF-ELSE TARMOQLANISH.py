# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:16:39 2024

@author: Baxtiyor
"""

# =============================================================================
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat
# tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring.
# GM uchun ikkala harfni katta qiling.
# =============================================================================

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
    
# if car=='gm': print(car.upper())
# else: print(car.title())
# print(cars.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#   if car=='gm':
#     print(car.upper())
#   else:
#     print(car.title())

# if car != 'gm': print(car.title())
# else: print(car.upper()) 

# =============================================================================
# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga
# chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# =============================================================================

# foydalanuvchi = ['Timur', 'Sardor']
# foydalanuvchi.append(input('Hurmatli foydalanuvchi login ismingizni kiriting, iltimos! \n>>>'))
# str user
# for f in foydalanuvchi:
#     if f.lower() != 'admin': 
#         print(f"Xush kelibsiz {f}!")
#     else: user = input("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")    
# if user == 'ha': 
#     print(foydalanuvchi())        
# if user != 'ha': 
#     print('Sog\' bo\'ling!') 
    
# =============================================================================
# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# =============================================================================

# a = float(input('1-sonni kiriting! \n >>> '))
# b = float(input('2-sonni kiriting! \n >>> '))
# if a==b: print('Sonlar teng!')
# if a>b: print('1-son 2-sondan katta!') 
# if a<b: print('1-son 2-sondan kichik!')

# =============================================================================
# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa 
# konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.    
# =============================================================================

# a = float(input('Hohlagan bir sonni kiriting! \n >>> '))
# if a>0: print('Musbat son!')
# else: print('Manfiy son!')

# =============================================================================
# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning 
# ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
# "Musbat son kiriting" degan xabarni chiqaring.
# =============================================================================

a = float(input('Hohlagan bir sonni kiriting! \n >>> '))

if a>0: print(f'Ushbu sonning ildizi {a**(1/2)} ga teng!')
else: print('Musbat son kiriting!')

