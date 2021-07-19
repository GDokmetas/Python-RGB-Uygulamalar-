
# #ffffff formatındaki hex renk kodunu programa uygun rgb formatına çevirir.

hex_string = input("Hex renk degerini giriniz... Ornek #FFFFFF")
kirmizi = hex_string[1:3]
yesil = hex_string[3:5]
mavi = hex_string[5:7]
kirmizi = int(kirmizi, 16)
yesil = int(yesil, 16)
mavi = int(mavi, 16)
print(kirmizi, yesil, mavi)