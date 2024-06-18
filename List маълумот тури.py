# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:35:17 2024
"""

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)

# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# =============================================================================
#                                    AMALIYOT
# =============================================================================
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = []
# ismlar.append("Oybek")
# ismlar.append("Farrux")
# ismlar.append("Olim")

# #Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
# print("Salom", ismlar[0], "bugun choyhona bormi?")
# print(ismlar[1], "choyhonaga boramizmi?")
# print(ismlar[2], "qaerdasiz?")

# sonlar deb nomlangan ro'yxat yarating
# va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# sonlar = []
# sonlar.append(23)
# sonlar.append(-23)
# sonlar.append(22)
# sonlar.append(21.1)

# # Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# # Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
# print(sonlar[0]+sonlar[1])
# print(sonlar[1]+sonlar[2])
# print(sonlar[3]*sonlar[0])
# print(sonlar[3]/sonlar[0])
# sonlar[1] = 323
# sonlar.insert(2, 24)
# del sonlar[4]

# print(sonlar)
# print(sonlar[-3])
# a = sonlar.pop(1)
# print(sonlar)
# b = sonlar.pop(2)
# print(sonlar, a + b)

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz 
# eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi
# tirik bo'lgan shaxslarning ismini kiriting.

# t_shaxslar = []
# z_shaxslar = []

# t_shaxslar.append('Chingizhan')
# t_shaxslar.insert(1, 'Tamerlan')
# t_shaxslar.insert(0, 'Jaloliddin')

# z_shaxslar.append('Mirza')
# z_shaxslar.append('Kadr')
# z_shaxslar.insert(0, 'Kebab')
# print(' Tarihiy shaxslar:', t_shaxslar, "\n", 'Zamonaviy shaxslar:', z_shaxslar)

# # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), 
# # quyidagi ko'rinishda chiqaring:
# print("Men tarihiy shaxslardan", t_shaxslar.pop(2), "bilan, zamonaviy shaxslardan esa", z_shaxslar.pop(1), "bilan suhbat qilishni istardim.")

# =============================================================================
# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta
# mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# =============================================================================

friends = []
friends.append("Gani")
friends.append("Gulom")
friends.append("Serdar")
friends.append("Kemal")
friends.append("Orhan")

# =============================================================================
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi
# yordamida o'chrib tashlang.
# =============================================================================

print(friends)
friends.remove("Kemal")
friends.remove("Serdar")
print(friends)

# =============================================================================
# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# =============================================================================

friends.append("Farrux")
friends.insert(0,"Farhod")
friends.insert(2,"Tarkan")
print(friends)

# =============================================================================
# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
# metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
# ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# =============================================================================

yangi_mehmonlar = ['Kamol', 'Akmal', 'Sarvar']
print(yangi_mehmonlar)

yangi_mehmonlar.append(friends.pop(0))
yangi_mehmonlar.append(friends.pop(2))
yangi_mehmonlar.append(friends.pop(3))
print("Yangi mehmonlar: ", yangi_mehmonlar)
print(yangi_mehmonlar[3])























