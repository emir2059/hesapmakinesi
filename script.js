function clearDisplay() {
    document.getElementById("display").value = "";
}

function deleteLast() {
    let display = document.getElementById("display");
    display.value = display.value.slice(0, -1);
}

function appendValue(value) {
    let display = document.getElementById("display");

    // Ekranda doğru sembolü göster
    if (value === '*') {
        display.value += '×';
    } else if (value === '/') {
        display.value += '÷';
    } else {
        display.value += value;
    }
}

function calculate() {
    let display = document.getElementById("display");
    try {
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        display.value = eval(expression);
    } catch {
        alert("Hatalı işlem!");
    }
}

function toggleMode() {
    document.body.classList.toggle("light-mode");
}

// --- Klavye girişi (sayfa yüklendiğinde bir kez ekle) ---
document.addEventListener("keydown", function(event) {
    let key = event.key;
    let display = document.getElementById("display");

    // Rakamlar
    if (/\d/.test(key)) {
        appendValue(key);
    }
    // İşlem tuşları
    else if (key === "+") {
        appendValue("+");
    } else if (key === "-") {
        appendValue("-");
    } else if (key === "*") {
        appendValue("*");
    } else if (key === "/") {
        appendValue("/");
    }
    // Enter = eşittir
    else if (key === "Enter") {
        calculate();
    }
    // Backspace = ⌫
    else if (key === "Backspace") {
        deleteLast();
    }
    // Escape = C tuşu
    else if (key === "Escape") {
        clearDisplay();
    }

    event.preventDefault();
});
function appendValue(value) {
    let display = document.getElementById("display");

    if (value === '*') {
        display.value += '×';
    } else if (value === '/') {
        display.value += '÷';
    } else {
        display.value += value; // parantez, . ve negatif sayılar buradan geçer
    }
}
function calculate() {
    let display = document.getElementById("display");
    try {
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        display.value = eval(expression); // parantez ve negatif sayılar artık çalışır
    } catch {
        alert("Hatalı işlem!");
    }
}
function square() {
    let display = document.getElementById("display");

    try {
        // Eğer ekranda sayı varsa onu kare al
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        let result = eval(expression); // mevcut ifade hesaplanır
        display.value = result * result; // kare al ve ekrana yaz
    } catch {
        alert("Hatalı işlem!");
    }
}
function reciprocal() {
    let display = document.getElementById("display");

    try {
        // Ekrandaki ifadeyi JS’in anlayacağı şekilde al
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        let result = eval(expression); // ifadeyi hesapla
        if (result === 0) {
            alert("Sıfıra bölme hatası!");
            return;
        }
        display.value = 1 / result; // tersini al ve ekrana yaz
    } catch {
        alert("Hatalı işlem!");
    }
}
function toggleSign() {
    let display = document.getElementById("display");

    if (display.value === "") return; // boşsa hiçbir şey yapma

    try {
        // Mevcut ifadeyi JS’in anlayacağı şekilde al
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        let result = eval(expression); // ifadeyi hesapla
        display.value = -result;       // işaret değiştir ve ekrana yaz
    } catch {
        alert("Hatalı işlem!");
    }
}
function appendValue(value) {
    let display = document.getElementById("display");

    if (value === '*') {
        display.value += '×';
    } else if (value === '/') {
        display.value += '÷';
    } else {
        display.value += value; // . , rakamlar ve parantez buradan geçer
    }
}
function percentage() {
    let display = document.getElementById("display");

    if (display.value === "") return; // boşsa hiçbir şey yapma

    try {
        // Ekrandaki ifadeyi JS’in anlayacağı şekilde al
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        let result = eval(expression); // ifadeyi hesapla
        display.value = result / 100;   // yüzdeye çevir ve ekrana yaz
    } catch {
        alert("Hatalı işlem!");
    }
}
let resultDisplayed = false; // sonuç gösterildi mi?
function calculate() {
    let display = document.getElementById("display");
    try {
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/');
        display.value = eval(expression);
        resultDisplayed = true; // sonuç gösterildi
    } catch {
        alert("Hatalı işlem!");
    }
}
function appendValue(value) {
    let display = document.getElementById("display");

    // Eğer sonuç gösterildiyse ve rakam/işlem giriliyorsa ekranı temizle
    if (resultDisplayed) {
        // Eğer girilen değer rakam veya nokta ise (yeni sayı başlıyor)
        if (/\d|\./.test(value)) {
            display.value = "";
        }
        resultDisplayed = false; // artık yeni giriş yapılıyor
    }

    // Ekranda doğru sembolü göster
    if (value === '*') {
        display.value += '×';
    } else if (value === '/') {
        display.value += '÷';
    } else {
        display.value += value;
    }
}
function appendPi() {
    let display = document.getElementById("display");

    // Eğer sonuç gösterildiyse ekranı temizle
    if (resultDisplayed) {
        display.value = "";
        resultDisplayed = false;
    }

    // Ekrana pi sembolü yaz
    display.value += 'π';
}
function calculate() {
    let display = document.getElementById("display");
    try {
        let expression = display.value
            .replace(/×/g, '*')
            .replace(/÷/g, '/')
            .replace(/π/g, Math.PI); // π’yi JS’in pi sayısına çevir

        display.value = eval(expression);
        resultDisplayed = true;
    } catch {
        alert("Hatalı işlem!");
    }
}
function squareRoot() {
    let display = document.getElementById("display");

    if (display.value === "") return; // boşsa hiçbir şey yapma

    try {
        // × ve ÷ işaretlerini JS’in anlayacağı şekilde al
        let expression = display.value.replace(/×/g, '*').replace(/÷/g, '/').replace(/π/g, Math.PI);
        let result = eval(expression);

        if (result < 0) {
            alert("Negatif sayının karekökü alınamaz!");
            return;
        }

        display.value = Math.sqrt(result); // karekök al ve ekrana yaz
        resultDisplayed = true; // sonuç gösterildi
    } catch {
        alert("Hatalı işlem!");
    }
}