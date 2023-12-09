#?i aylık yol masrafımızı hesaplayan bir program yazmak istiyoruz. Elimizdeki verilerin
#şunlar olduğunu varsayalım:
#!1. Cumartesi-Pazar günleri çalışmıyoruz.
#!2. Dolayısıyla ayda 22 gün çalışıyoruz.
#!3. Evden işe gitmek için kullandığımız vasıtanın ücreti 1.5 TL
#!4. İşten eve dönmek için kullandığımız vasıtanın ücreti 1.4 TL

# gun=31
# gidis=1.5
# donus=1.4
# hesapla=gun*(gidis+donus)
# print(hesapla)


#gidiş ve dönüş ücretini kendimiz belirlerse şu şekilde yapabiliriz

# gidis_ucret=float(input("Gidiş ücretinizi giriniz:"))
# donus_ucret=float(input("Dönüş ücretinizi giriniz:"))
# hesaplaUcret=gun*(gidis_ucret+donus_ucret)
# print(hesaplaUcret)

#! Kullanıcının girdiği sayının karesini alan program

# karesi=int(input("bir sayı giriniz: "))
# hesapla_Karesi=karesi**2
# print("Sayının Karesinin Sonucu {} ".format(hesapla_Karesi))


#Bir sayının üssünü almak için pythonda hazır olarak gelen modüller vardır pow() fonksiyonu
#bir sayının üssünü alabiliriz
print (pow(3,2))

#!pow fonksiyonu üç değer alır ilk değer sayı ikinci sayı
#!kuvvetini üçüncüsü ise sayının kuvvetini aldıktan sonra
#!çıkan sayının üçüncü parametrye ne değer verdiysek bölme 
#! işleminden kalan sonucu gösterir

print(pow(10,3,2)) #10 sayısının 3. kuvetinin sonucunun 2 ile bölümünden kalanı verir


#aynı değerlere sahip değişkenler şu şekilde kısa yol ile tanımlanabilir
# a=4
# b=4
# a=b=4 #kısa yolu 


#bir yıl içindeki her bir ayın çektiği gün sayısını ay adlarına atayabilirsiniz:
ocak=mart=mayıs=temmuz=ağustos=ekim=aralık=31
# nisan=haziran=eylül=kasım=30
# şubat=28
# print(şubat)


#Mart ayı doğalgaz faturasına göre sayaçtan ölçülen hacim 346 m3
#Demek ki bir ayda toplam
#346 m3 doğalgaz harcamışız.
#Fatura tutarı 273.87 TL imiş. Yani 346 m3 doğalgaz tüketmenin bedeli 273.87 TL. Buna göre
#değişkenlerimizi tanımlayalım:

fatura_tutari=273.87
m_3=346

#!Bu bilgiyi kullanarak doğalgazın birim fiyatını hesaplayabiliriz. Formülümüz şöyle olmalı:
birim_fiyat = fatura_tutari/m_3
print(birim_fiyat)

#!Demek ki doğalgazın m3 fiyatı (vergilerle birlikte yaklaşık) 0.79 TL’ye karşılık geliyormuş.
#!Bu noktada günlük ortalama doğalgaz sarfiyatımızı da hesaplamamız gerekiyor:

gunluk=m_3/mart
print(gunluk)
#Demek ki Mart ayında günlük ortalama 11 m3 doğalgaz tüketmişiz.

#şimdi ise Bir sonraki ayın faturasını tahmin etmek için python kodunu yazalım 
#bu sefer tarihler datetime modülünden çekelim 
#geçmiş aydaki fatura miktarlarıda 150, 180, 200, 220, 190

#?import datetime ifadesi kullanıldığında, datetime modülünün tüm sınıfları ve 
#?fonksiyonları projede kullanılabilir hale gelir. Bu sayede, tarihlerin oluşturulması,
#?tarihler arasında hesaplamalar yapılması, saat bilgilerinin elde edilmesi gibi 
#?işlemler için datetime modülündeki fonksiyonlardan ve sınıflardan faydalanılabilir.

# datetime.date(year, month, day): Belirtilen yıl, ay ve gün bilgilerine 
# dayanan bir datetime.date nesnesi oluşturur.

# datetime.datetime(year, month, day, hour, minute, second, microsecond): 
# Belirtilen yıl, ay, gün, saat, dakika, saniye ve mikrosaniye bilgilerine
# dayanan bir datetime.datetime nesnesi oluşturur.

# datetime.time(hour, minute, second, microsecond): Belirtilen saat, dakika, saniye ve
# mikrosaniye bilgilerine dayanan bir datetime.time nesnesi oluşturur.

# datetime.timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks): 
# Belirtilen gün, saniye, mikrosaniye, milisaniye, dakika, saat veya hafta gibi bir zaman 
# aralığını temsil eden bir timedelta nesnesi oluşturur.

# datetime.date.today(): Şu anki yerel tarihi döndüren bir datetime.date nesnesi oluşturur.

# datetime.datetime.now(): Şu anki yerel tarih ve saat bilgisini döndüren bir
# datetime.datetime nesnesi oluşturur.

# datetime.datetime.strptime(date_string, format): Belirtilen bir tarih dizesini,
# belirtilen biçime göre bir datetime.datetime nesnesine dönüştürür.

import datetime
#geçmiş ayın faturalarını bir liste halina aldık
gecmis_faturalar=[150, 180, 200, 220, 190]

#gelecek ayın tarihini hesaplıyoruz
bugun= datetime.datetime.today() #Burada bugun değişkeni, datetime.date.today() fonksiyonunu kullanarak şu anki tarihi temsil eden bir datetime.date nesnesidir.
gelecek_ay=datetime.date(bugun.year, bugun.month+ 1, 1) # şu anki tarihten bir ay sonrasının tarihini hesaplamak için kullanılır.

#bugun.month + 1 ifadesi, şu anki ayın bir fazlasını temsil eder. Böylece bir sonraki ayın sayısını elde etmiş oluruz.
#Son olarak, datetime.date(bugun.year, bugun.month + 1, 1) ifadesi, şu anki yılın aynı olmasını, ayın bir fazlasını ve günün 1 olmasını sağlayarak bir sonraki ayın 
# ilk gününün tarihini temsil eden bir datetime.date nesnesi oluşturur.

#! Geçmiş ayların fatura ortalamasını alalım
ortalama=sum(gecmis_faturalar)/len(gecmis_faturalar)

# Tahmin edilen fatura miktarını ekrana yazdıralım

print("Tahmin edilen gelecek ayın fatura miktarı:", ortalama)


#!Girilen Üç Sayının yazılı ortalamasını alan programı ekrana yazdıran python kodunu ekrana yazdıran program

# sayi1=int(input("Bir Notunuzu giriniz:"))
# sayi2=int(input("İkinci Notunuzu giriniz:"))
# sayi3=int(input("Üçüncü Notunuzu giriniz:"))
# ortalama=(sayi1+sayi2+sayi3)/3
# print(f"Girilen Notların Ortalaması:{ortalama}")


#!if ile ilgili Örnekler

#Yazılı Ortalaması girilen öğrencinin sınıf geçme durumunu (Geçti Kaldı) olarak gösteren kod


# yazili=int(input("Yazılı Ortalamasını Giriniz:"))
# if(yazili>=50):
#     print("Geçtiniz")
# else:
#     print("Kaldınız")


#!Girilen Sayının Tek mi Çift mi Olduğunu Bulan Python Örneği

sayi=int(input("Bir sayı giriniz:"))
if(sayi%2==0):
    print(f"Girilen Sayı : {sayi} çiftir ")
else:
    print(f"Girilen Sayı:{sayi} tektir")

#Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bulan Python Örneği
sayiDurum=int(input("bir sayı giriniz"))
if(sayiDurum<0):
    print(f"Girilne sayı {sayiDurum} negatiftir.")
elif(sayiDurum>0):
    print(f"Girilen sayı :{sayiDurum} pozitiftir")
else:
    print(f"Girilen sayı:{sayiDurum}")
    
    


#Kullanıcıdan (1-4) arasında sayı alınacak, bu sayıya göre sırasıyla ilkbahar-yaz-sonbahar-kış yazan python örneği

syigir=int(input(f"""
           1 ile 4 arasında bir sayı giriniz:
           "
           1:İlkbahar
           2:Yaz
           3:Sonbahar
           4:Kış
           "
           """))
if(syigir==1):
    print("İlkbahar")
elif(syigir==2):
    print("Yaz")
elif(syigir==3):
    print("Sonbahar")
elif(syigir==4):
    print("Kış")
else:
    print("sadece 1 ile 4 arasında sayı girebilirsiniz")


