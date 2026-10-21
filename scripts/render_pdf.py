"""Render the same HTML as an A4 PDF using a local Chromium browser."""
from pathlib import Path
import argparse, os, shutil, subprocess, tempfile

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--browser',help='Chrome or Edge executable')
args=parser.parse_args()
candidates=[args.browser,os.environ.get('CHROME_BIN'),shutil.which('google-chrome'),shutil.which('chromium'),
 r'C:\Program Files\Google\Chrome\Application\chrome.exe',
 r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe']
browser=next((p for p in candidates if p and Path(p).is_file()),None)
if not browser: raise SystemExit('Chrome/Chromium/Edge not found. Pass --browser PATH.')
pdf=root/'docs/hana_multi_asset_portfolio.pdf'
with tempfile.TemporaryDirectory(prefix='hana-print-') as profile:
    result=subprocess.run([browser,'--headless=new','--disable-gpu','--no-first-run',
        '--no-default-browser-check',f'--user-data-dir={profile}',
        '--no-pdf-header-footer','--allow-file-access-from-files',
        f'--print-to-pdf={pdf}',(root/'docs/index.html').as_uri()],
        capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=60)
    if result.returncode or not pdf.is_file():
        raise SystemExit(result.stderr)
try:
    from pypdf import PdfReader
    reader=PdfReader(pdf)
    if len(reader.pages)!=5: raise SystemExit(f'Expected 5 pages, got {len(reader.pages)}')
    for page in reader.pages:
        if abs(float(page.mediabox.width)-595.28)>1 or abs(float(page.mediabox.height)-841.89)>1:
            raise SystemExit('Expected A4 portrait')
    print(f'Created A4 PDF: {len(reader.pages)} pages')
except ImportError:
    print('Created PDF. Install pypdf to check the page count.')
