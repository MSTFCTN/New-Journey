
import time
print("Hello World!")
time.sleep(1)

print("Lütfen isminizi girin!")

x = input()

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("Hoşgeldin " + x +" !" )

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("Hadi şimdi birden ona kadar sayalım !")
z = range(1,11,1)
for n in z:
    print(n)
    time.sleep(0.3)

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("Şimdi gireceğimiz sayıların eşit olup olmadığına bakacağız")

time.sleep(0.5)
print("...")
time.sleep(0.5)

print("a ve b sayılarını sırasıyla girin:")
time.sleep(0.7)
a = int(input("A = "))
time.sleep(0.2)
b = int(input("B = "))
time.sleep(0.5)

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)
 
while(a!=b):
    print(a==b)
    time.sleep(0.7)
    print("lütfen birbirine eşit olan a ve b sayılarını giriniz")
    time.sleep(0.5)
    print("a ve b sayılarını sırasıyla girin:")
    time.sleep(0.5)
    a = int(input("A = "))
    time.sleep(0.3)
    b = int(input("B = "))
    time.sleep(0.5)

    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
print(a==b)
time.sleep(0.7)
print("Tebrikler!")

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("1'den 10'a kadar olan asal sayıların toplamını yazınız (2,3,5,7).")
toplam = int(input())

while(toplam!=17):

    print(".")
    time.sleep(0.3)
    print("..")
    time.sleep(0.3)
    print("...")
    time.sleep(0.3)

    print("Yanlış Sonuç!")
    time.sleep(0.5)
    print("Tekrar deneyin:")
    toplam= int(input())

time.sleep(0.5)
print(".")
time.sleep(0.3)
print("..")
time.sleep(0.3)
print("...")
time.sleep(0.3)

print("Tebrikler doğru sonucu buldunuz :)")

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("Şimdi bir üçgenin alanını nasıl buluruz ona bakalım")

time.sleep(0.5)
print("...")
time.sleep(1)

print("Bir üçgenin alanını bulmak için bir taban belirleyip ardından o tabanın karşısındaki bir köşeden tabana dik olaran inen bir yükseklik bulmalıyız. Daha sonra taban ve yüksekliği çarpıp ikiye bölmeliyiz.")

time.sleep(0.5)
print("...")
time.sleep(2)

print("Artık üçgenin alanını bulmayı öğrendiğimize göre hadi biraz hesap yapalım!")

time.sleep(1)
print("...")
time.sleep(1)


taban=float(input("lütfen üçgeninizin taban uzunluğunu girin: "))

time.sleep(0.2)
print("...")
time.sleep(0.7)

yukseklik=float(input("lütfen üçgeninizin yüksekliğini girin: "))

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(1)

alan = (taban * yukseklik) / 2

print("Üçgenin alanı = "+ str(alan))

time.sleep(0.5)
print(".")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print("...")
time.sleep(0.5)

print("Finito!")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)