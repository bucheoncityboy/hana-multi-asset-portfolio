"""Generate the static GitHub Pages portfolio and editable Markdown."""
from pathlib import Path
import json
import html
import hashlib

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
PROFILE = DATA['profile']
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)
esc = html.escape
CSS_VERSION = hashlib.sha256((OUT/'styles.css').read_bytes()).hexdigest()[:12]
JS_VERSION = hashlib.sha256((OUT/'app.js').read_bytes()).hexdigest()[:12]

def lis(items):
    return '<ul>' + ''.join('<li>' + esc(x) + '</li>' for x in items) + '</ul>'

def link(label, url, cls=''):
    return f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)} <span aria-hidden="true">↗</span></a>'

def section_title(number, title):
    return f'<h2 class="profile-section-title"><span>{number}</span>{esc(title)}</h2>'

education_rows = ''.join(
    '<tr>' + ''.join(f'<td>{esc(e[key])}</td>' for key in ['school', 'major', 'period', 'status']) + '</tr>'
    for e in PROFILE['education']
)
credential_rows = ''.join(
    f'<tr><td class="credential-type">{esc(c["type"])}</td><td>{esc(c["name"])}</td><td>{esc(c["date"])}</td></tr>'
    for c in PROFILE['credentials']
)
activity_rows = ''.join(
    f'<article class="activity-row"><header class="profile-row-heading"><h3>{esc(a["name"])}</h3><p class="period">{esc(a["period"])}</p></header>{lis(a["items"])}</article>'
    for a in PROFILE['activities']
)
experience = PROFILE['experience']
profile_page = f'''<section class="profile sheet" id="overview" aria-labelledby="profile-name">
  <header class="profile-header"><div class="profile-heading"><h1 id="profile-name">{esc(DATA['name'])}</h1><div class="application-target"><strong>{esc(PROFILE['organization'])}</strong><p>{esc(PROFILE['department'])}</p></div><p class="document-title">{esc(PROFILE['title'])}</p></div><p class="english-title">{esc(PROFILE["englishTitle"])}</p><p class="profile-summary">{' <span aria-hidden="true">/</span> '.join(esc(x) for x in PROFILE['summary'])}</p></header>
  <section class="profile-block education">{section_title('01', '학력')}<div class="table-scroll"><table class="profile-table education-table"><caption class="sr-only">학력</caption><colgroup><col class="school-col"><col class="major-col"><col class="period-col"><col class="status-col"></colgroup><thead><tr><th scope="col">학교</th><th scope="col">전공</th><th scope="col">기간</th><th scope="col">비고</th></tr></thead><tbody>{education_rows}</tbody></table></div></section>
  <section class="profile-block activities">{section_title('02', '교내 활동')}{activity_rows}</section>
  <section class="profile-block credentials">{section_title('03', '자격증 및 수료')}<div class="table-scroll"><table class="profile-table credentials-table"><caption class="sr-only">자격증 및 수료 내역</caption><colgroup><col class="type-col"><col><col class="date-col"></colgroup><thead><tr><th scope="col">구분</th><th scope="col">내용</th><th scope="col">취득일</th></tr></thead><tbody>{credential_rows}</tbody></table></div></section>
  <section class="profile-block experience">{section_title('04', '실무 경험')}<div class="experience-row"><header class="profile-row-heading"><h3>{esc(experience['name'])}</h3><p class="period">{esc(experience['period'])}</p></header><p class="experience-details"><span>{esc(experience['items'][0])} / {esc(experience['items'][1])}</span><strong>{esc(experience['items'][2])}</strong></p></div></section>
  <section class="profile-block core-skills">{section_title('05', '핵심 역량')}<ul class="skill-list">{''.join(f'<li>{esc(x)}</li>' for x in PROFILE['competencies'])}</ul></section>
  <p class="print-folio">김재원 · 하나자산운용 멀티에셋솔루션팀 지원 포트폴리오 <span>01 / 05</span></p>
</section>'''

nav = '<a class="nav-link active" href="#overview"><span>01</span>프로필 및 핵심 역량</a>' + ''.join(f'<a class="nav-link" href="#{p["id"]}"><span>{p["number"]}</span>{esc(p["navTitle"])}</a>' for p in DATA['projects'])
projects = []
for p in DATA['projects']:
    table = ''
    if 'table' in p:
        t=p['table']
        table='<figure class="result-table"><table><caption>'+esc(t['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(x)+'</td>' for x in row)+'</tr>' for row in t['rows'])+'</tbody></table><figcaption>'+esc(t['note'])+'</figcaption></figure>'
    flow='<ol class="decision-flow" aria-label="투자 의사결정 과정">'+''.join('<li>'+esc(x)+'</li>' for x in p['flow'])+'</ol>' if 'flow' in p else ''
    print_layout = ''
    projects.append(f'''<section class="project sheet{print_layout}" id="{p['id']}" aria-labelledby="title-{p['id']}">
      <header class="project-header"><span class="chapter">{p['number']}</span><div><p class="eyebrow">{esc(p['category'])}</p><h2 id="title-{p['id']}">{esc(p['title'])}</h2><p class="subtitle">{esc(p['subtitle'])}</p></div></header>
      <p class="project-summary">{esc(p['summary'])}</p>
      {flow}<div class="overview-block"><h3>프로젝트 개요</h3><dl class="meta"><div><dt>수행 형태</dt><dd>{esc(p['type'])}</dd></div><div><dt>수행 기간</dt><dd>{esc(p['period'])}</dd></div><div class="wide"><dt>프로젝트 목표</dt><dd>{esc(p['goal'])}</dd></div><div class="wide scope"><dt>검증 범위</dt><dd>{esc(p['scope'])}</dd></div></dl></div>
      <div class="project-columns"><div class="project-main"><div class="text-block"><h3>데이터 및 설계</h3>{lis(p['design'])}</div><div class="text-block"><h3>주요 수행 내용</h3>{lis(p['work'])}</div></div>
      <aside class="results"><p class="result-kicker">검증 결과 및 성과</p><p class="result-metric">{esc(p['metric'])}</p><p class="metric-label">{esc(p['metricLabel'])}</p>{table}{lis(p['results'])}<p class="scope-note">{esc(p['note'])}</p></aside></div>
      <footer class="project-links"><h3>관련 자료</h3>{link('GitHub 저장소',p['repo'],'repo-link')}<div class="evidence-links">{''.join(link(*x) for x in p['links'])}</div></footer>
      <p class="print-folio">김재원 · 하나자산운용 멀티에셋솔루션팀 지원 포트폴리오 <span>{int(p['number']):02d} / 05</span></p>
    </section>''')

document = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#006f6b"><title>김재원 | 하나자산운용 지원 포트폴리오</title><meta name="description" content="글로벌 ETF 자산배분, 시장 브리핑, 미국 대형주 운용자료 관리와 기업 리서치 지원 경험을 정리한 김재원의 포트폴리오입니다."><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css?v={CSS_VERSION}"><script src="app.js?v={JS_VERSION}" defer></script></head>
<body><a class="skip-link" href="#main">본문으로 이동</a><div class="reading-progress" aria-hidden="true"></div>
<aside class="sidebar"><a href="#overview" class="identity"><span class="identity-label">지원 포트폴리오</span><strong>김재원<span class="identity-dot">.</span></strong><span class="identity-en">JAEWON KIM</span></a><nav aria-label="포트폴리오 목차">{nav}</nav><div class="sidebar-bottom"><p>GLOBAL MULTI-ASSET<br>RESEARCH &amp; OPERATIONS</p><div class="download-links"><a href="hana_multi_asset_portfolio.pdf" download>PDF 내려받기 ↓</a><a href="hana_multi_asset_portfolio.md" download>Markdown 원본 ↓</a></div></div></aside>
<main id="main">{profile_page}
{''.join(projects)}<footer class="site-footer"><span>김재원 · 지원 포트폴리오</span><a href="hana_multi_asset_portfolio.pdf" download>PDF 내려받기 ↓</a><a href="#overview">처음으로 ↑</a></footer></main></body></html>'''
(OUT / 'index.html').write_text(document,encoding='utf-8')
(OUT / '.nojekyll').write_text('',encoding='utf-8')

md = f'# {PROFILE["organization"]} {PROFILE["title"]}\n\n**{DATA["name"]} | {PROFILE["organization"]} {PROFILE["department"]}**\n\n'
md += PROFILE['englishTitle'] + '\n\n'
md += ' / '.join(PROFILE['summary']) + '\n\n## 01. 학력\n\n| 학교 | 전공 | 기간 | 비고 |\n| --- | --- | --- | --- |\n'
md += ''.join('| ' + ' | '.join(e[k] for k in ['school', 'major', 'period', 'status']) + ' |\n' for e in PROFILE['education'])
md += '\n## 02. 교내 활동\n\n'
for a in PROFILE['activities']:
    md += f'### {a["name"]} | {a["period"]}\n\n' + '\n'.join('- '+x for x in a['items']) + '\n\n'
md += '## 03. 자격증 및 수료\n\n| 구분 | 내용 | 취득일 |\n| --- | --- | --- |\n'
md += ''.join(f'| {c["type"]} | {c["name"]} | {c["date"]} |\n' for c in PROFILE['credentials'])
md += f'\n## 04. 실무 경험\n\n**{experience["name"]} | {experience["period"]}**\n\n' + '\n'.join('- '+x for x in experience['items'])
md += '\n\n## 05. 핵심 역량\n\n' + '\n'.join('- '+x for x in PROFILE['competencies'])+'\n\n'
for p in DATA['projects']:
    md += f'---\n\n## [{int(p["number"])}. {p["title"]}]\n\n**프로젝트: {p["subtitle"]}**\n\n### 프로젝트 개요\n\n'
    md += p['summary'] + '\n\n'
    if 'flow' in p: md += ' → '.join(p['flow']) + '\n\n'
    for label,key in [('수행 형태','type'),('수행 기간','period'),('프로젝트 목표','goal'),('검증 범위','scope')]:
        md += f'- **{label}:** {p[key]}\n'
    for title,key in [('데이터 및 설계','design'),('주요 수행 내용','work'),('검증 결과 및 성과','results')]:
        if key == 'results':
            md += '\n**'+p['metric']+' | '+p['metricLabel']+'**\n\n'
            if 'table' in p:
                t=p['table']
                md += t['caption']+'\n\n| '+' | '.join(t['headers'])+' |\n| '+' | '.join(['---']*len(t['headers']))+' |\n'
                md += ''.join('| '+' | '.join(row)+' |\n' for row in t['rows'])+'\n'+t['note']+'\n'
        md += '\n### '+title+'\n\n'+'\n'.join('- '+x for x in p[key])+'\n'
    md += '\n> '+p['note']+'\n\n### 관련 자료\n\n'+f'- [GitHub 저장소]({p["repo"]})\n'+'\n'.join(f'- [{label}]({url})' for label,url in p['links'])+'\n\n'
for path in [ROOT/'hana_multi_asset_portfolio.md',OUT/'hana_multi_asset_portfolio.md']:
    path.write_text(md,encoding='utf-8')
print('Generated docs/index.html and Markdown source (4 projects).')
