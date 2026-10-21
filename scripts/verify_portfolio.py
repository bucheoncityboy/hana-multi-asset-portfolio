"""Verify content parity, local downloads, page count, and public evidence links."""
from pathlib import Path
from html.parser import HTMLParser
import json,re,subprocess,argparse,concurrent.futures

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--links',action='store_true',help='Verify GitHub evidence paths with authenticated gh CLI')
args=parser.parse_args()
data=json.loads((root/'content.json').read_text(encoding='utf-8'))
web=(root/'docs/index.html').read_text(encoding='utf-8')
md=(root/'hana_multi_asset_portfolio.md').read_text(encoding='utf-8')
assert md==(root/'docs/hana_multi_asset_portfolio.md').read_text(encoding='utf-8')
class Text(HTMLParser):
    def __init__(self):super().__init__();self.parts=[];self.links=[];self.ids=[];self.sheetparts=[];self.depth=0
    def handle_data(self,s):
        self.parts.append(s)
        if self.depth:self.sheetparts.append(s)
    def handle_starttag(self,t,a):
        a=dict(a)
        if t=='section':
            if 'sheet' in a.get('class','').split():self.depth=1
            elif self.depth:self.depth+=1
        if 'href' in a:self.links.append(a['href'])
        if 'id' in a:self.ids.append(a['id'])
    def handle_endtag(self,t):
        if t=='section' and self.depth:self.depth-=1
h=Text();h.feed(web)
flat=' '.join(h.parts)
norm=lambda s:re.sub(r'\s+','',s)
for term in ['이지스','igis','VFS','vfs']:
    assert term not in web and term not in md and term not in json.dumps(data,ensure_ascii=False)
for p in data['projects']:
    for k in ['title','subtitle','summary','type','period','goal','scope','metric','metricLabel','note']:
        assert norm(p[k]) in norm(flat),(p['id'],k,'html')
        assert norm(p[k]) in norm(md),(p['id'],k,'md')
    for k in ['design','work','results']:
        for value in p[k]:assert norm(value) in norm(flat) and norm(value) in norm(md),(p['id'],k)
for url in h.links:
    if url.startswith('#'):assert url[1:] in h.ids,url
    elif not url.startswith('http'):assert (root/'docs'/url.split('?')[0]).is_file(),url
from pypdf import PdfReader
pdf=PdfReader(root/'docs/hana_multi_asset_portfolio.pdf')
assert len(pdf.pages)==5
pdf_text='\n'.join(page.extract_text() for page in pdf.pages)
for i,page in enumerate(pdf.pages):
    assert abs(float(page.mediabox.width)-595.28)<1 and abs(float(page.mediabox.height)-841.89)<1
    expected='김재원' if i==0 else data['projects'][i-1]['title']
    assert norm(expected) in norm(page.extract_text())
for part in h.sheetparts:
    s=part.strip()
    if not s or s in ['↗','↓','↑'] or 'PDF 내려받기' in s or 'Markdown 원본' in s or s in ['지원 포트폴리오','JAEWON KIM','본문으로 이동','자격증 및 수료 내역','GLOBAL MULTI-ASSET','RESEARCH & OPERATIONS','처음으로 ↑']:continue
    # Navigation labels are shorter alternatives; download controls are screen-only.
    if s in [p['navTitle'] for p in data['projects']]+['프로필 및 핵심 역량']:continue
    assert norm(s) in norm(pdf_text),('missing in PDF',s)
report={'date':'2026-10-22 Asia/Seoul','a4_portrait_pages':5,'content_parity':'PASS','internal_links':'PASS'}
report_manifest=root/'verification/report-links.json'
if report_manifest.is_file():
    import hashlib
    reports=json.loads(report_manifest.read_text(encoding='utf-8'))['reports']
    annotations=[a.get_object().get('/A',{}).get('/URI') for page in pdf.pages for a in page.get('/Annots',[])]
    for item in reports:
        path=root/item['local_file']
        assert path.is_file() and path.read_bytes().startswith(b'%PDF-')
        assert len(PdfReader(path).pages)==item['pages']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256']
        assert item['url'] in h.links and item['url'] in md and item['url'] in annotations
    assert not any('/blob/' in str(uri) and str(uri).endswith('.html') for uri in annotations)
    report['readable_report_pdf_links']='PASS'
    report['report_pdf_count']=len(reports)
if args.links:
    def check(url):
        parts=url.removeprefix('https://github.com/').split('/')
        owner,repo=parts[:2]
        endpoint=f'repos/{owner}/{repo}'
        if len(parts)>2 and parts[2]=='blob':endpoint+='/contents/'+'/'.join(parts[4:])+'?ref='+parts[3]
        elif len(parts)>2 and parts[2]=='pull':endpoint+='/pulls/'+parts[3]
        result=subprocess.run(['gh','api',endpoint,'--silent'],capture_output=True,text=True,encoding='utf-8')
        return {'url':url,'ok':result.returncode==0}
    urls=sorted({u for u in h.links if u.startswith('https://github.com/')})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:checks=list(pool.map(check,urls))
    report['evidence_links']=checks
    assert all(c['ok'] for c in checks),[c for c in checks if not c['ok']]
(root/'verification/build-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='evidence_links'},ensure_ascii=False))
if args.links:print('Verified evidence links:',len(checks))

