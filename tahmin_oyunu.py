import random as rd

_author_ = "PourLa"
print("TAHMİN ETME OYUNU")
pc=rd.randrange(0,100)
hak = 0

while True:
 try:

   while True:
    tahmin=int(input("0-100 arasında bir sayı giriniz:"))
    hak += 1

    if pc==tahmin :
       print("Tam isabet, Tahmininiz Doğru")
       print("Kullanılan hak : {}".format(hak))
       input("ENTER'a basınız!")
       break

    elif pc<tahmin :
       print("Daha küçük bir sayı giriniz")
       print ("Kullanılan hak : {}".format (hak))

    elif pc>tahmin :
       print("Daha büyük bir değer giriniz")
       print ("Kullanılan hak : {}".format (hak))

    else :
      print("Lütfen bir Sayı giriniz!")
      print ("Kullanılan hak : {}".format (hak))

   break

 except ValueError:
    print("Lütfen sadece sayı girin!")