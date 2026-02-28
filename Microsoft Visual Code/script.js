// Durum değişkeni: Sonuç yeni mi hesaplandı?
let resultDisplayed = false;

// 1. Değer Ekleme Fonksiyonu
function appendValue(value) {
    const display = document.getElementById("display");
    
    if (resultDisplayed) {
        // Eğer sonuç ekranındaysak ve sayıya basıldıysa ekranı temizle
        if (/\d|\.|\π/.test(value)) {
            display.value = "";
        }
        resultDisplayed = false;
    }

    if (value === '*') display.value += '×';
    else if (value === '/') display.value += '÷';
    else display.value += value;
    
    display.focus();
}

// 2. Pi Sayısı Ekleme
function appendPi() {
    appendValue('π');
}

// 3. Hesaplama (Eşittir)
function calculate() {
    const display = document.getElementById("display");
    try {
        let expression = display.value
            .replace(/×/g, '*')
            .replace(/÷/g, '/')
            .replace(/π/g, Math.PI);
            
        if (expression.trim() === "") return;
        
        display.value = eval(expression);
        resultDisplayed = true;
    } catch (e) {
        alert("Hatalı İşlem!");
        display.value = "";
    }
    display.focus();
}

// 4. Karesini Alma (x²) - HATANIN ÇÖZÜMÜ
function square() {
    const display = document.getElementById("display");
    try {
        let val = eval(display.value.replace(/×/g, '*').replace(/÷/g, '/').replace(/π/g, Math.PI));
        display.value = val * val;
        resultDisplayed = true;
    } catch { alert("Hata!"); }
    display.focus();
}

// 5. Tersini Alma (1/x) - HATANIN ÇÖZÜMÜ
function reciprocal() {
    const display = document.getElementById("display");
    try {
        let val = eval(display.value.replace(/×/g, '*').replace(/÷/g, '/').replace(/π/g, Math.PI));
        display.value = 1 / val;
        resultDisplayed = true;
    } catch { alert("Hata!"); }
    display.focus();
}

// 6. Yüzde (%) - HATANIN ÇÖZÜMÜ
function percentage() {
    const display = document.getElementById("display");
    try {
        let val = eval(display.value.replace(/×/g, '*').replace(/÷/g, '/').replace(/π/g, Math.PI));
        display.value = val / 100;
        resultDisplayed = true;
    } catch { alert("Hata!"); }
    display.focus();
}

// 7. Temizleme ve Silme
function clearDisplay() {
    document.getElementById("display").value = "";
    document.getElementById("display").focus();
}

function deleteLast() {
    const display = document.getElementById("display");
    display.value = display.value.slice(0, -1);
    display.focus();
}

// 8. İşaret Değiştirme (+/-)
function toggleSign() {
    const display = document.getElementById("display");
    if (display.value.startsWith('-')) {
        display.value = display.value.substring(1);
    } else {
        display.value = '-' + display.value;
    }
}

// 9. Karekök (√)
function squareRoot() {
    const display = document.getElementById("display");
    try {
        let val = eval(display.value.replace(/×/g, '*').replace(/÷/g, '/').replace(/π/g, Math.PI));
        display.value = Math.sqrt(val);
        resultDisplayed = true;
    } catch { alert("Hata!"); }
    display.focus();
}

// 10. Tema Değiştirme
function toggleMode() {
    document.body.classList.toggle("light-mode");
}