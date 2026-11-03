const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2]));
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
  for (const j of jobs) {
    await p.goto('file://' + j.html, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(150);
    await p.screenshot({ path: j.png });
  }
  await b.close();
})();
