import random as rd

_author_ = "PourLa"
print("TAHMİN ETME OYUNU")

pc = rd.randrange(0, 100)
hak = 0

while True:
    try:
        tahmin = int(input("0-100 arasında bir sayı giriniz: "))
        hak += 1

        if pc == tahmin:
            print("Tam isabet, Tahmininiz Doğru!")
            print("Kullanılan hak: {}".format(hak))
            break
        elif pc < tahmin:
            print("Daha küçük bir sayı giriniz.")
        elif pc > tahmin:
            print("Daha büyük bir değer giriniz.")

        print("Kullanılan hak: {}".format(hak))

    except ValueError:
        print("Lütfen sadece sayı girin!")
