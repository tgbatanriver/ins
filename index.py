#ekrana 'Hello World" yazdıran kodu yazınız

print("Helllo World")


#?Ekranda "neosyazilim.com" yazacak kodu yazınız

print("neosyazilim"+".com")


#Ekranda yan yana isminizi ve soy isminizi yazdıracak python kodunu yazdırınız

print("Tuğba"+ " " +"Tanrıver")
print("Tuğba" + " Tanrıver")  #Burada da Tanrıver karakter dizisinin başına bir adet boşluk yerleştirerek istediğimiz çıktıyı elde ettik

#?Ekranda üç kere kendi isminizi yazdırabileceğiniz python kodunu yazınız


#!Birinci yöntem
isim="Tuğba "
sonuc=isim * 3
print(sonuc)


#!İkinci Yöntem
print("Tuğba " * 3)


#Ekrana  'uzak     çok uzak...' yazdıracak python kodunu yazdırın(5 adet boşluk)

#!Birinci yöntem
print("uzak     "+"çok uzak...")

#!İkinci Yöntem
print("uzak"+ " "*5 +"çok uzak...")


# ekrana 23 ve 35  birleşik yazdıracak python kodu

print("23"+"35")   #burada bir karakter dizesidir eğer bunları tırnak işareti içerisine almasaydık 
                   #bir sayı dizesi olacaktı karakter dizeleri ve sayı dizeleri pythonda yan yana birleşik
                   #yazılamazlar
#print("23"+35) => burada hata alırsınız. Asla unutmayın, aritmetik işlemler ancak
#sayılar arasında yapılır. Karakter dizileri ile herhangi bir aritmetik işlem yapılamaz.



#? İsminizin ve Soyisminizin kaç karakter uzunluğuna geldiğini bulan python kodu 

isim_soyisim="Tuğba Tanrıver"
print(len(isim_soyisim.replace(' ', '')))


# "Dünya" kelimesinin tipini bulan python kodu

content="Dünya"
print(type(content))


# İki değişkenimiz olsun biri kullanıcı adı ve diğeri parola bunların karakter uzunluğu 40 karakteri aşmasının 
#40 karakteri aşıp aşmadığını nasıl kontrol ederiz python kodunu yazınız örneğin kullanıcı adı=mavi  parola=neosyazilim123

kullanici_adi="mavi"
parola="neosyazilim123"
print(len(kullanici_adi) + len(parola))

#burada len type sayı değerli bir veri göndermesi sayesinde ikisi uzunluğunu sayabiliyoruz

# print(type(len(kullanici_adi)))

#aşşağıda gösterilenleri değişken ismi olarak kullanmazsınız
import keyword
yasakli=keyword.kwlist
print(yasakli)

#Örneğin type değişken olarak kullandığınızda type değişkenmiş gibi davranıcak ve bir değerin tipini 
#incelemek istediğinizde hata alacaksınız dolayısıyla eğer type bir değişken olarak kullanacaksanız 
#type değerini tekrar değişke olarak kullanmak istediğimiz şu şekilde bir çözüm üretilir


type=345 #dediğimizde bunun type değeri hata gönderecek 
#print(type(type))

#şu komut yardımıyla type değişkenini ortadan kaldırmış oluruz

del type

#!Böylece, (tahmin edebileceğiniz gibi delete (silmek) kelimesinin kısaltması olan) del
#!komutuyla type değişkenini silmiş oldunuz. Artık ‘type’ kelimesi yine type() fonksiyonunu çağıracak:

print(type(type))

# #len içinde aynı şekilde hata ile karşılaşacaksının bunun içinse şu şekilde bir çözüm üretebiliriz 

# my_list = [1, 2, 3, 4, 5]
# length = len(my_list)
# print(length)  # 5

# # len değişkenine farklı bir değer atadığımızda, orijinal len işlevi geçici olarak kaybolur
# len = "tgb"
# print(len)  # tgb

# # Orijinal len işlevine tekrar erişmek için "builtins" modülünü kullanabiliriz
# import builtins

# # Şimdi len işlevini tekrar kullanabiliriz
# length = builtins.len(my_list)
# print(length)  # 5


#!bultins metodu 
#Yerleşik işlevleri içerisinde barındırır
#Yerleşik işlevler , Python programlama
# dilinde başlangıçtan itibaren kullanılabilen ve önceden tanımlanmış olan işlevlerdir.
# Bu işlevler, Python'ın temel işlevlerini gerçekleştirir
# ve genellikle genel programlama görevlerini kolaylaştırmak için kullanılır.
#Python dilinde yerleşik olarak sunulan işlevler arasında 
# len, print, type, range, sum, max, min, abs, round gibi işlevler bulunur. 
# Bu işlevler, programın herhangi bir yerinde kullanılmak üzere hazır olarak 
# gelir ve herhangi bir ek içe aktarma veya modül yükleme gerektirmez.
#Python dilinde yerleşik işlevler, herhangi bir modül veya paket içe aktarma işlemi yapmadan doğrudan kullanılabilir.
# Bu işlevler, Python yorumlayıcısının kendisi tarafından sağlanır ve 
# standart kütüphane ile birlikte gelir.


#peki neden tekrar kullandık hazır olarak geliyorsa 
#!Evet, builtins modülünü kullanarak len işlevini değişken olarak kullandığımız için yeniden etkinleştirmek için import ile dahil ettik.
#!builtins modülü, Python dilinde yerleşik işlevlere ve nesnelere erişmemizi sağlar.
#!Bu modül, yerleşik işlevleri içeren bir modül 
#!olduğu için len işlevine erişmek için builtins modülünü kullanabiliriz.


#! Soru: 25,30,45 sayılarıyla  7030, 2575, 10025 olarak yazdıran kod.

# x = "25"
# y = "30"
# z = "45"
# sonuc1=str(int(x)+int(z)) + y
# print(sonuc1)
# sonuc2=x+str(int(y)+int(z))
# print(sonuc2)
# sonuc3=str(int(x)+int(y)+int(z))+x
# print(sonuc3)



#Girilen kullanıcı ismine göre ekrana “Merhaba Kullanıcı” yazdıran python kodunu yazınız.
# ad=input("Kullanıcı adınızı giriniz:")
# print("Merhaba", ad)


#! Ad ve Soyad bilgilerinin inputtan alındığı kodu yazınız (format metodu ile)
# ad=input("Adınızı Giriniz:")
# soyad=input("Soyad Giriniz:")
# print(f"Adını {ad} Soyadınız {soyad}")
# print("ad: {}\nsoyad: {}".format(ad, soyad)) #\n bir alt satıra inemenizi sağlar

#Klavyeden girilen iki sayıyı toplayan ve sonucu ekranda gösteren python kodunu yazınız.
# toplam=0;
# x1=float(input("Birinci sayıyı giriniz:"))
# x2=float(input("İkinci sayıyı giriniz:"))
# toplam=x1+x2
# print(toplam)