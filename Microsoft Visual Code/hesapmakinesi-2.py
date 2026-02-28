import math
import math
while True:
    try:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /, %, //, **): ")

        if islem == "+":
            print("Sonuç:", sayi1 + sayi2)

        elif islem == "-":
            print("Sonuç:", sayi1 - sayi2)

        elif islem == "*":
            print("Sonuç:", sayi1 * sayi2)

        elif islem == "/":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                if sonuc.is_integer():
                    print("Sonuç:", int(sonuc))
                else:
                    print("Sonuç:", round(sonuc, 2))  # küsuratlı ise 2 basamak yuvarla
            else:
                print("Bir sayı sıfıra bölünemez!")

        elif islem == "%":
            if sayi2 != 0:
                print("Sonuç:", sayi1 % sayi2)
            else:
                print("Bir sayı sıfıra bölünemez!")

        elif islem == "//":
            if sayi2 != 0:
                print("Sonuç:", sayi1 // sayi2)
            else:
                print("Bir sayı sıfıra bölünemez!")

        elif islem == "**":
            print("Sonuç:", sayi1 ** sayi2)

        else:
            print("Geçersiz işlem!")

    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

    devam = input("Başka işlem yapmak istiyor musunuz? (e/h): ").lower()
    if devam != "e":
        print("Hesap makinesinden çıkılıyor...")
        break
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /, %, //, **): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)

elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)

elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)

elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        if sonuc.is_integer():
            print("Sonuç:", int(sonuc))
        else:
            print("Sonuç:", sonuc)
    else:
        print("Hata: 0’a bölme!")

elif islem == "%":
    if sayi2 != 0:
        print("Sonuç:", sayi1 % sayi2)
    else:
        print("Hata: 0’a bölme!")

elif islem == "//":
    if sayi2 != 0:
        print("Sonuç:", sayi1 // sayi2)
    else:
        print("Hata: 0’a bölme!")

elif islem == "**":
    print("Sonuç:", sayi1 ** sayi2)

else:
    print("Geçersiz işlem!")
print("Hızlı Bilimsel Hesap Makinesi")
print("Örnek: 10 + 5, 2 * 3, 10 / 2, 2 ** 3, 10 % 3")
print("Trigonometrik ve özel fonksiyonlar için: sin(30), cos(60), tan(45), sqrt(9), 10^3, e^2")
print("Faktöriyel ve logaritma: 5!, log(100), ln(2.71828)")
print("Çıkmak için: q\n")

while True:
    islem = input("İşlemi gir: ").lower()

    if islem == "q":
        print("Hesap makinesinden çıkılıyor...")
        break

    islem = islem.replace("^", "**")                  
    islem = islem.replace("e^", "math.e**")          
    islem = islem.replace("sqrt", "math.sqrt")       
    islem = islem.replace("sin", "math.sin(math.radians")  
    islem = islem.replace("cos", "math.cos(math.radians")  
    islem = islem.replace("tan", "math.tan(math.radians")  

    # Faktöriyel için
    if "!" in islem:
        try:
            n = int(islem.replace("!", ""))
            if n >= 0:
                print("Sonuç:", math.factorial(n))
            else:
                print("Hata: Faktöriyel için pozitif tam sayı girin!")
        except:
            print("Geçersiz faktöriyel ifadesi!")
        print("\n--- Yeni işlem ---\n")
        continue

    # Log ve ln için
    if "log(" in islem:
        islem = islem.replace("log(", "math.log10(")
    if "ln(" in islem:
        islem = islem.replace("ln(", "math.log(")

    try:
        sonuc = eval(islem + (")" * islem.count("(")))  # eksik parantezleri kapat
        print("Sonuç:", sonuc)
    except ZeroDivisionError:
        print("Hata: 0’a bölme!")
    except Exception as e:
        print("Geçersiz işlem! Hata:", e)

    print("\n--- Yeni işlem ---\n")

print("Hızlı Hesap Makinesi")
print("Örnek: 10 + 5, 2 * 3, 10 / 2, 2 ** 3, 10 % 3")
print("Trigonometrik ve özel fonksiyonlar için: sin(30), cos(60), tan(45), sqrt(9), 10^3, e^2")
print("Çıkmak için: q\n")

while True:
    islem = input("İşlemi gir: ").lower()

    if islem == "q":
        print("Hesap makinesinden çıkılıyor...")
        break

    # Özel ifadeleri Python formatına çevirelim
    islem = islem.replace("^", "**")     # 10^3 -> 10**3
    islem = islem.replace("e^", "math.e**")  # e^2 -> math.e** 
    islem = islem.replace("sqrt", "math.sqrt")  # sqrt(9) -> math.sqrt(9)
    islem = islem.replace("sin", "math.sin(math.radians")  # sin(30) -> math.sin(math.radians(30
    islem = islem.replace("cos", "math.cos(math.radians")  # cos(60) -> math.cos(math.radians(60
    islem = islem.replace("tan", "math.tan(math.radians")  # tan(45) -> math.tan(math.radians(45

    try:
        sonuc = eval(islem + (")" * islem.count("(")))  # eksik parantezleri kapat
        print("Sonuç:", sonuc)
    except ZeroDivisionError:
        print("Hata: 0’a bölme!")
    except Exception as e:
        print("Geçersiz işlem! Hata:", e)

    print("\n--- Yeni işlem ---\n")
print("Bilimsel Hesap Makinesi\n")
print("İşlemler:")
print("İki sayılı: + - * / % // **")
print("Tek sayılı: sin, cos, tan, 10^, e, log, ln, sqrt, !")
print("Çıkmak için: q\n")

while True:
    islem = input("İşlemi gir: ").lower()

    if islem == "q":
        print("Hesap makinesinden çıkılıyor...")
        break

    if islem in ["sin", "cos", "tan", "10^", "e", "log", "ln", "sqrt", "!"]:
        x = float(input("Sayıyı gir: "))

        if islem == "sin":
            print("Sonuç:", math.sin(math.radians(x)))
        elif islem == "cos":
            print("Sonuç:", math.cos(math.radians(x)))
        elif islem == "tan":
            print("Sonuç:", math.tan(math.radians(x)))
        elif islem == "10^":
            print("Sonuç:", 10 ** x)
        elif islem == "e":
            print("Sonuç:", math.e ** x)
        elif islem == "log":
            if x > 0:
                print("Sonuç:", math.log10(x))
            else:
                print("Hata: logaritma için pozitif sayı girin!")
        elif islem == "ln":
            if x > 0:
                print("Sonuç:", math.log(x))
            else:
                print("Hata: ln için pozitif sayı girin!")
        elif islem == "sqrt":
            if x >= 0:
                print("Sonuç:", math.sqrt(x))
            else:
                print("Hata: karekök için negatif sayı girilemez!")
        elif islem == "!":
            if x >= 0 and x.is_integer():
                print("Sonuç:", math.factorial(int(x)))
            else:
                print("Hata: faktöriyel için pozitif tam sayı girin!")

    else:
        sayi1 = float(input("Birinci sayıyı gir: "))
        sayi2 = float(input("İkinci sayıyı gir: "))

        if islem == "+":
            print("Sonuç:", sayi1 + sayi2)
        elif islem == "-":
            print("Sonuç:", sayi1 - sayi2)
        elif islem == "*":
           print("Sonuç:", sayi1 * sayi2)
    if sayi2 != 0:
        sonuc = sayi1 / sayi2  
        if sonuc.is_integer():
            print("Sonuç:", int(sonuc))  
        else:
            print("Sonuç:", sonuc)       
    else:
        print("Hata: 0’a bölme!")
    if sayi2 != 0:
        print("Sonuç:", sayi1 % sayi2)
    else:
        print("Hata: 0’a bölme!")

