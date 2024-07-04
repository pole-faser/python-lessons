# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 17:28:29 2024
18-DARS. WHILE, RO'YXATLAR VA LUG'ATLAR
@author: Baxtiyor
"""

# =============================================================================
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# =============================================================================
# savat =[]
# n=1

# while True:    
#     buyurtma = input(f"Iltimos {n}-buyurtmani kiriting! \n>>>").lower()
#     savat.append(buyurtma)
#     savol = input("Yana buyurtma qilasizmi? (Ha/Yo'q)").lower()
#     if savol == "ha":
#         n+=1
#         continue
#     else: break
# print(f"Sizning buyurtmalaringiz quyidagilar: "
#       f"{savat}")

# # =============================================================================
# # e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# # Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# # =============================================================================
# e_bozor = {}
# n=1
# # while True:
# #     key = input(f"Iltimos, {n}-mahsulot nomini kiriting! ").lower()
# #     value = input(f"Iltimos, {n}-mahsulot narxini kiriting! ").lower()
# #     e_bozor[key] = int(value)
# #     savol = input("Dasturni tugatgan bo'lsangiz '+' bosing, yo'qsa istalgan tugmani bosing!").lower()
# #     if savol != "+": 
# #         n+=1       
# #         continue
# #     else:
# #         break
# print("Rahmat!")
# =============================================================================
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan
# solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# =============================================================================
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")