import fs from 'fs';
import QRCode from 'qrcode-svg';

const data = fs.readFileSync('data', 'utf8').split('\n');
const QRdata = data[data.length - 4];
const STdata = data[data.length - 2];

const QRsvg= new QRCode(QRdata).svg().split('\n').slice(0,-1);;
const STbin = Array.from(STdata).map((c) => c.charCodeAt(0).toString(2).padStart(8, '0')).join('');

for (let i = 0; i < STbin.length; i++) {
    if (i+2 < QRsvg.length) {
        QRsvg[i+2] = QRsvg[i+2].replace('<rect', `<rect rx="${STbin[i]}"`);
    } else {
        QRsvg.push(`<rect rx="${STbin[i]}"/>`)
    }
}
QRsvg.push('</svg>');

console.log(QRsvg.join('\n'));
