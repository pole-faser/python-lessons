# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:11:54 2024
19-DARS. FUNKSIYA
@author: Baxtiyor
"""

# =============================================================================
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# =============================================================================
# def yosh_hisobla(ism, yosh, j_yil=2024):
#     """
#     ism :       Foydalanuvchi ismi.
#     yosh :      Foydalanuvchi yoshi.
#     Returns:    Tugilgan yili chiqarib beradi.
#     """
    
#     print(f"Hurmatli {ism}, Siz {j_yil-yosh} yilda tug'lgansiz!")


# ism = input(f"Ismingizni kiriting! ").title()
# yosh = int(input(f"Hurmatli {ism} yoshingizni kiriting! "))
# yosh_hisobla(ism, yosh)

# =============================================================================
# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# =============================================================================

# def kv_kub_hisobla(son):
#     """Foydalanuvchi bergan sonning kvadrat va kubini chiqaruvchi"""
#     print(f"{son}ning kvadrati: {son**2} \n"
#           f"{son}ning kubi: {son**3}")

# son1 = int(input("Iltimos biror son kiriting! "))
# kv_kub_hisobla(son1)

# =============================================================================
# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# =============================================================================
# def juft_toq_aniqla(qiymat):
#     """ Berilgan sonning juft yoki toqligini aniqlovchi funktsiya"""
#     rich = bool 
#     if qiymat%2 !=0: print(f"{qiymat} toq son!")
#     else: print(f"{qiymat} juft son!")

# son2 = int(input("Iltimos biror son kiriting! "))
# juft_toq_aniqla(son2)

# =============================================================================
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# =============================================================================
def kattani_top(son11, son22):
    if son11>son22: print(f"{son11} katta!")
    elif son11==son22: print("Sonlar teng")
    else: print(f"{son22} katta!")
    
son11 = float(input("1-sonni kiriting! "))
son22 = float(input("2-sonni kiriting! "))
kattani_top(son11, son22)
