// Rebuild optimized website images from the preserved generated PNG sources.
// Run with Node.js and the sharp package available.
const fs = require('fs');
const path = require('path');
let sharp;
try { sharp = require('sharp'); }
catch { sharp = require('/Users/chaselobosco/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp'); }
const root = path.resolve(__dirname, '..');
const records = JSON.parse(fs.readFileSync(path.join(__dirname, 'manifest.json'), 'utf8')).assets;
const output = path.join(root, 'website/images/photos');
fs.mkdirSync(output, { recursive: true });
(async () => {
  let bytes = 0;
  for (const record of records) {
    const source = path.join(root, record.source);
    if (!fs.existsSync(source)) throw new Error('Missing original: ' + record.source);
    for (const width of [640, record.w]) {
      const height = Math.round(width * record.h / record.w);
      const suffix = width === 640 ? '-640' : '';
      for (const format of ['jpg', 'webp']) {
        const target = path.join(output, record.file + suffix + '.' + format);
        // Standard web resize/crop; original pixels are preserved in generated-assets/originals.
        const pipe = sharp(source).resize(width, height, { fit: 'cover', position: 'centre' });
        if (format === 'jpg') await pipe.jpeg({ quality: 84, mozjpeg: true }).toFile(target);
        else await pipe.webp({ quality: 82, effort: 5 }).toFile(target);
        bytes += fs.statSync(target).size;
      }
    }
  }
  console.log(JSON.stringify({ photos: records.length, exports: records.length * 4, totalMB: (bytes / 1048576).toFixed(2) }));
})().catch(error => { console.error(error); process.exit(1); });
