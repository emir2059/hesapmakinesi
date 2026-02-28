# 🧮 Web Tabanlı Hesap Makinesi

Bu proje, Visual Studio Code kullanılarak geliştirilmiş, modern arayüzlü bir hesap makinesidir.

## 🖼️ Uygulama Görseli
![Hesap Makinesi](ekran-goruntusu.png)

## ✨ Özellikler
* Temel matematiksel işlemler (Toplama, Çıkarma, Çarpma, Bölme)
* Temizleme (AC) fonksiyonu
* Responsive (Mobil uyumlu) tasarım

## 🛠️ Kullanılan Teknolojiler
* **HTML5:** Sayfa yapısı
* **CSS3:** Tasarım ve animasyonlar
* **JavaScript:** Hesaplama mantığı

## 🚀 Canlı Önizleme
Projeyi canlı olarak buradan görebilirsiniz:
[file:///C:/Users/tkumb/OneDrive/Masa%C3%BCst%C3%BC/Microsoft%20Visual%20Code/index.html]

---
*Bu proje eğitim amaçlı geliştirilmiştir.*
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hesap Makinesi</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<div class="calculator">
    <input type="text" id="display" disabled>

    <div class="buttons">
        <button onclick="clearDisplay()">C</button>
        <button onclick="appendValue('/')">÷</button>
        <button onclick="appendValue('*')">×</button>
        <button onclick="deleteLast()">⌫</button>
        <button onclick="appendValue('(')">(</button>
<button onclick="appendValue(')')">)</button>
<button onclick="square()">X²</button>
<button onclick="reciprocal()">1/x</button>
<button onclick="toggleSign()">+/-</button>
<button onclick="appendValue('.')">.</button>
<button onclick="percentage()">%</button>
<button onclick="appendPi()">π</button>
<button onclick="squareRoot()">√</button>

        <button onclick="appendValue('7')">7</button>
        <button onclick="appendValue('8')">8</button>
        <button onclick="appendValue('9')">9</button>
        <button onclick="appendValue('-')">−</button>

        <button onclick="appendValue('4')">4</button>
        <button onclick="appendValue('5')">5</button>
        <button onclick="appendValue('6')">6</button>
        <button onclick="appendValue('+')">+</button>

        <button onclick="appendValue('1')">1</button>
        <button onclick="appendValue('2')">2</button>
        <button onclick="appendValue('3')">3</button>
        <button onclick="calculate()" class="equal">=</button>

        <button onclick="appendValue('0')" class="zero">0</button>
        <button onclick="appendValue('.')">.</button>
        <div class="mode-toggle">
    <button onclick="toggleMode()">🌙 / ☀️</button>
</div>
    </div>
</div>

<script src="script.js"></script>
</body>
</html>
