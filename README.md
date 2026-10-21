# 하나자산운용 멀티에셋솔루션팀 지원 포트폴리오

김재원의 글로벌 금융시장 리서치, ETF 자산배분, 운용자료 관리 및 기업 리서치 지원 경험을 정리한 정적 웹사이트입니다.

- 웹: https://bucheoncityboy.github.io/hana-multi-asset-portfolio/
- PDF: [A4 세로 5페이지](docs/hana_multi_asset_portfolio.pdf)
- Markdown: [웹과 같은 콘텐츠](hana_multi_asset_portfolio.md)
- 검증 근거: [출처·확인 범위](verification/source-notes.md), [소스 커밋·F141 CSV 대조·PR 병합 기록](verification/sources.json), [최종 증빙 대조 결과](verification/final-audit.json)

기업분석 페이지의 두 보고서 링크는 `docs/reports/`에 보관한 공개 구버전 PDF로 바로 연결합니다. GitHub의 HTML 소스 화면을 보고서 열람 링크로 사용하지 않습니다. 원본과 동일한 파일이며 출처·SHA-256은 `verification/report-links.json`에 기록합니다.

## 구성

1. 프로필 및 핵심 역량
2. 글로벌 ETF 자산배분 연구: 8 ETF와 BIL, F141의 141개월 결과
3. 글로벌 시장 브리핑 AI 자동화: 공식 원천·거래일·기준일 검증
4. 미국 대형주 전략 및 운용 시스템: 목표 비중·주문자료·Excel 원장
5. 기업분석 AI 에이전트: 공시·실적자료 대조와 출처 기록

## 편집과 빌드

Python 3.10 이상을 사용합니다. 별도 웹 프레임워크나 외부 API 키가 필요하지 않습니다.

```powershell
python build.py
python -m http.server 8000 --directory docs
```

`content.json`이 콘텐츠의 단일 원본입니다. `build.py`는 `docs/index.html`과 루트·docs의 Markdown을 함께 생성합니다. Markdown을 직접 고치면 다음 빌드에서 덮어씁니다. `docs/styles.css`와 `docs/app.js`는 기존 보고서 레이아웃과 목차 기능을 유지합니다. 폰트는 시스템의 맑은 고딕·Apple SD Gothic Neo·Noto Sans KR 순으로 사용합니다.

## PDF 갱신

웹 콘텐츠나 스타일을 고친 뒤 반드시 PDF도 갱신합니다. Chrome·Chromium·Edge가 필요하며 동일한 HTML과 인쇄 CSS를 사용합니다.

```powershell
python scripts/render_pdf.py
# 브라우저를 찾지 못하면:
python scripts/render_pdf.py --browser "C:\Program Files\Google\Chrome\Application\chrome.exe"
```

선택적으로 `pip install pypdf`를 실행하면 PDF 생성 후 정확히 5페이지인지, A4 세로인지 검사합니다. 브라우저 수동 인쇄 시 A4, 배율 100%, 머리글·바닥글 끄기, 배경 그래픽 켜기를 적용합니다. 내용이 늘면 페이지 수 검사를 통과하도록 문장과 인쇄 여백을 조정한 뒤 페이지별 렌더링도 확인합니다. 페이지를 강제로 잘라 숨기는 방식은 사용하지 않습니다.

`pypdf` 설치 후 `python scripts/verify_portfolio.py`로 웹·Markdown·PDF의 본문 일치, 로컬 내려받기 경로와 5페이지를 검사합니다. GitHub CLI 인증이 있으면 `--links`를 추가해 공개 증빙 링크도 확인할 수 있습니다.

## GitHub Pages 배포

별도 공개 저장소 `bucheoncityboy/hana-multi-asset-portfolio`의 `main` 브랜치 `/docs`를 배포 소스로 사용합니다. GitHub 저장소 Settings → Pages → Deploy from a branch → `main` / `/docs` → Save에서 설정할 수 있습니다.

```powershell
git add content.json build.py docs hana_multi_asset_portfolio.md README.md verification scripts .gitignore
git commit -m "Update multi-asset portfolio"
git push origin main
```

소스 편집 후 `python build.py`와 PDF 갱신을 먼저 실행합니다. PDF·Markdown 내려받기는 상대경로를 사용하므로 GitHub Pages 하위 경로에서도 작동합니다. 원문 자소서·이력서·개인 계좌 로그·연락처는 저장소에 포함하지 않습니다.

## 사실관계와 한계

F141은 `korean-macro-factor-allocation`의 `long / primary / cost_bp=5` 결과를 사용합니다. 별도 `global-etf-regime-allocation`의 12 ETF·117개월 수치는 사용하지 않습니다. CER는 위험을 반영한 지표이며 연 수익률·CAGR와 구분합니다. 로지스틱 대비 XGBoost의 통계적 우위는 확인되지 않았습니다. 같은 F141 평가 기준에서 국면 없는 평균분산의 연 CER는 4.69%, SPY/IEF 60/40은 7.00%로, 국면 예측 전략이 모든 비교군을 앞선 것은 아닙니다.

브리핑 시간 단축은 학회원 피드백으로 통제 실험이 아닙니다. 개인 프로젝트를 기관 펀드 운용 경험으로 표현하지 않습니다. 로컬 실행 로그의 매수 29건·매도 1건은 Excel 실행결과표의 상태·수량·평균가·주문 식별자와 일치했습니다. 이는 같은 애플리케이션 내부 기록의 대조이며 브로커 원본에 따른 실제 체결의 독립 검증은 아닙니다. 매도 29건과 실계좌 수익률은 확인되지 않았습니다. 계좌번호·주문 식별자·실제 거래내역 원본은 공개하지 않습니다.

기업분석 v3.0의 2026.08.31 README에는 19개 종목의 커버리지 목록이 있습니다. 다만 19개 지원 구현이나 19개 전체의 분석 완료를 검증한 자료와 구분해, 포트폴리오에 지원 수치를 복원하지 않았습니다. 두산에너빌리티·셀트리온 샘플의 문서 표기일은 2026.07.03이고 v3.0 자료입니다. 현재 v3.2 스킬의 가상 실행 예제와 구분합니다.

원 연구를 재학습하거나 운용 시스템의 실제 주문을 실행하지 않았습니다. 검증은 저장소 자료·코드·산출물의 대조와 이번 포트폴리오의 빌드·출력·링크 확인을 대상으로 합니다.
