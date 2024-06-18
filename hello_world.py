# print("Hello World!")
# print("Assalomu aleakum")
# print('Hayrli tong!')
# print(2+4*2)
# print(19/5)
# print(2**4)
print('"Nexia", "Tico", \'Damas\' ko\'rganlar qilar havas')

#5 ning 4-darajasini toping
print('5 ning 4-darajasi', 5**4, 'ga teng.') 

#22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print('22 ni 4 ga bo\'lganda', 22%4, 'qoldiq qoladi') 

#22 ni 4 ga bo'lganda?
print('22 ni 4 ga bo\'lganda javobi', 22/4, 'ga teng') 

#Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
#kvadratning yuzi
print("Tomonlari 125 ga teng kvadratning yuzi", 125*125, "ga teng") 

#kvadratning perimetri
print("kvadratning perimetri", 125*4, "ga teng") 

#Diametri 12 ga teng bo'lgan doiraning yuzini toping (π=3.14 deb oling)
#S = π * r² = π * (d/2)² = π * (d²/4)
print("Diametri 12 ga teng bo'lgan doiraning yuzi", (3.14*(12/2)**2), "ga teng")

#Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping
print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi", (6**2+7**2)**(1/2), "ga teng")

#"Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
matn="Hello World!"
print(matn)

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, 
# keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar='biror matn'
print(xabar)
xabar='2-matn'
print(xabar)

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va
# konsolga chiqaring (siz kutgan natija chiqdimi?)

radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
print("Assalom alaykum, ", ism.title())


