import math

def hesap_makinesi():
    print("--- Gelişmiş Bilimsel Hesap Makinesi ---")
    print("İşlemler: +, -, *, /, %, //, **, sqrt, sin, cos, tan, log, ln, !")
    print("Çıkış için 'q' yazın.\n")

    while True:
        islem = input("Yapılacak işlemi veya operatörü girin: ").lower().strip()

        if islem == 'q':
            print("Hesap makinesinden çıkılıyor...")
            break

        try:
            # Tek sayı gerektiren işlemler (Bilimsel)
            if islem in ["sin", "cos", "tan", "log", "ln", "sqrt", "!"]:
                x = float(input(f"{islem} işlemi için sayıyı girin: "))
                
                if islem == "sin":
                    print(f"Sonuç: {math.sin(math.radians(x))}")
                elif islem == "cos":
                    print(f"Sonuç: {math.cos(math.radians(x))}")
                elif islem == "tan":
                    print(f"Sonuç: {math.tan(math.radians(x))}")
                elif islem == "log":
                    print(f"Sonuç: {math.log10(x)}" if x > 0 else "Hata: Pozitif sayı girin!")
                elif islem == "ln":
                    print(f"Sonuç: {math.log(x)}" if x > 0 else "Hata: Pozitif sayı girin!")
                elif islem == "sqrt":
                    print(f"Sonuç: {math.sqrt(x)}" if x >= 0 else "Hata: Negatif sayı girilemez!")
                elif islem == "!":
                    if x >= 0 and x.is_integer():
                        print(f"Sonuç: {math.factorial(int(x))}")
                    else:
                        print("Hata: Pozitif tam sayı girin!")

            # İki sayı gerektiren standart işlemler
            elif islem in ["+", "-", "*", "/", "%", "//", "**"]:
                sayi1 = float(input("Birinci sayıyı girin: "))
                sayi2 = float(input("İkinci sayıyı girin: "))

                if islem == "+": print(f"Sonuç: {sayi1 + sayi2}")
                elif islem == "-": print(f"Sonuç: {sayi1 - sayi2}")
                elif islem == "*": print(f"Sonuç: {sayi1 * sayi2}")
                elif islem == "/":
                    if sayi2 != 0:
                        sonuc = sayi1 / sayi2
                        print(f"Sonuç: {int(sonuc) if sonuc.is_integer() else round(sonuc, 4)}")
                    else:
                        print("Hata: Sıfıra bölme!")
                elif islem == "%": print(f"Sonuç: {sayi1 % sayi2}")
                elif islem == "//": print(f"Sonuç: {sayi1 // sayi2}")
                elif islem == "**": print(f"Sonuç: {sayi1 ** sayi2}")

            else:
                print("Geçersiz işlem tipi!")

        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin!")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

        print("\n" + "-"*20 + "\n")

if __name__ == "__main__":
    hesap_makinesi()