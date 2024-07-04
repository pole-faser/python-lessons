# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:41:30 2024
17-DARS. while TSIKLI
@author: Baxtiyor
"""

# =============================================================================
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# =============================================================================

# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "
# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')

# =============================================================================
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki,
# dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# =============================================================================
# savol = "\nYoshingiz nechida? (Dasturdan chiqish uchun exit yoki quit deb yozing!) \n>>>"
# go = True
# while go:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit':
#         print('Rahmat!') 
#         go = False
#         break
    
#     q = int(yosh)    
#     if q<7: narx = 2000
#     elif 7<=q<18: narx = 3000
#     elif 18<=q<65: narx = 10000
#     else: narx = 0
    
#     if narx == 0: 
#         print("Sizga chipta bepul!")
#     else:    
#         print(f"Siz uchun chipta narhi {narx} so'm!")
     
# #if go == False: print('Rahmat!')


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.lower() =='exit':
        break
    son = float(qiymat)
    if son!=0:
        ildiz = son**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")