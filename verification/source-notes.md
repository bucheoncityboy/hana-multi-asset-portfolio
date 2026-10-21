# 출처 대조와 편집 판단

확인일: 2026-10-21 (한국시간)

## 지원 직무

[인턴 공식 공고](https://www.kofia.or.kr/brd/m_96/view.do?seq=42668)의 글로벌 경제·기업/산업·금융시장 리서치 지원, 글로벌 펀드 운용 보조를 기준으로 구성했다. [동일 팀 경력직 공고](https://www.kofia.or.kr/brd/m_96/view.do?seq=40642)의 글로벌 자산배분 EMP 및 해외 펀드 관련 업무는 팀의 업무 배경을 이해하는 데만 참고했다. 펀드 설정·환매·F/X·기관 RFP를 인턴 확정 업무나 지원자의 수행 경력으로 기재하지 않았다. Bloomberg 활용 경험과 영어 능력은 새로 추정해 추가하지 않았다.

## 프로필과 문체

기존 포트폴리오 `content.json`의 학력·학회·자격·수료·링커리어 경험을 재사용했다. 로컬의 기존 자소서 아카이브 PDF 34~38페이지와 수행 내용·문장 구조를 대조했다. 2026.09 ETF 연구 기간, 브리핑의 사용 피드백, 개인 운용과 코드 검증의 구분을 유지했다. 연락처·생년월일·주소 등은 공개 파일에 추가하지 않았다. 개인 원문은 이 저장소에 포함하지 않는다.

## ETF 자산배분

- [README](https://github.com/bucheoncityboy/korean-macro-factor-allocation), [F141 CSV](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/results/followup/summary.csv), [전체 결과](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/docs/followup.md), [데이터 명세](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/docs/data.md)를 대조했다.
- CSV에서 `cohort=long`, `policy=primary`, `cost_bp=5`, `months=141`로 필터링하고 표의 네 CER를 대조했다. 기간은 2014.01~2025.09, 위험자산은 8 ETF와 현금 BIL이다.
- 연 CER는 자산2 로지스틱 2.11%, 자산2 XGBoost 2.69%, 경제4 로지스틱 6.62%, 경제4 XGBoost 5.90%다. 경제4 XGBoost와 자산2 XGBoost의 차이는 3.21%p이나 국면 정의·표적이 다른 비교다. 두 국면 모두 XGBoost의 로지스틱 대비 통계적 우위는 확인되지 않았다.
- 일반 수익률로 오해하지 않도록 CER를 정의했다. 원문 동일자료 재현·전향 검증으로 표현하지 않았다. 시장자료의 과거 수정 빈티지 복원 한계를 명시했다.
- F141 비교표가 5페이지 보고서에서 읽기 쉬워 본문에 사용하고 기존 NAV·낙폭 차트는 증빙 링크로 연결했다. [별도 후속 저장소](https://github.com/bucheoncityboy/global-etf-regime-allocation)의 12 ETF·117개월 결과는 본문 수치에 혼합하지 않았다.

## 글로벌 브리핑

[README](https://github.com/bucheoncityboy/multi-asset-morning-briefing), `scripts/market_data.py`, 테스트와 규칙 문서를 확인했다. 미국 재무부·Cboe·ECB·ECOS를 우선 사용하며 FRED는 지연을 확인하는 보조 원천이다. 약 40분→10분 이내는 자소서·사용자 제공 내용의 학회원 피드백으로 통제 실험이 아니다.

K-Skill PR [675](https://github.com/NomaDamas/k-skill/pull/675), [682](https://github.com/NomaDamas/k-skill/pull/682), [683](https://github.com/NomaDamas/k-skill/pull/683), [684](https://github.com/NomaDamas/k-skill/pull/684), [685](https://github.com/NomaDamas/k-skill/pull/685)의 작성자와 `merged_at`을 API로 대조했다. 브리핑은 2026.09.19, 나머지 네 PR은 2026.09.30에 병합됐다. 정식 기능 채택·금융 리서치 스킬 5종 기여 표현은 이 기록에 한정한다.

## 미국 대형주 운용자료

[최신 README](https://github.com/bucheoncityboy/us-robust-live-ops), 공통 정책·주문 검증·Excel 생성 코드와 [9개 결함 수정 기록](https://github.com/bucheoncityboy/us-robust-live-ops/blob/main/docs/audit_fixes.md)을 확인했다. 공개 Excel 템플릿 자체는 6개 시트이며 현재 `ops/ops_excel_write.py`가 `06_Weekly_Trend`를 추가해 7개 시트를 구성하는 경로를 확인했다. 7개 시트는 현재 코드 구성에 대한 표현이며 템플릿 파일의 시트 수와 구분한다. 포트폴리오 증빙 링크도 현재 생성 코드로 연결했다. WFA 구현과 과거 시장 성과 재산출의 한계를 구분하고 구형/수정 전 백테스트 수익률은 포트폴리오에서 제외했다.

공개 저장소는 실제 브로커 체결과 실계좌 수익률을 미검증으로 표시한다. 추가로 로컬 과거 운용 로그를 읽기 전용으로 확인했다. 한 파일에 매수 29건의 `FILL / FILLED` 기록이 있고 다른 파일에는 매도 1건과 오류 기록이 있으나, 매도 29건과 브로커 원본 대조 기록은 확인되지 않았다. 애플리케이션 로그만으로 계좌 실체·전체 주문·원장 일치까지 독립 검증할 수 없어 매수·매도 각 29건을 성과에 반영하지 않았다. 개인 로그·계좌/주문 식별자·체결 상세는 공개 저장소에 복사하지 않았다. 실제 주문 실행은 하지 않았다.

## 기업 리서치

[현재 README](https://github.com/bucheoncityboy/agentic-research-pipeline)와 v3.2 코드의 계산·검수·출처 기록을 확인했다. 최신 배포본에서 고정 19개 종목 지원 목록은 확인되지 않아 수치를 제외했다. [두산에너빌리티](https://github.com/bucheoncityboy/agentic-research-pipeline/blob/main/archive/v3.0/doosan-enerbility-20260703.html), [셀트리온](https://github.com/bucheoncityboy/agentic-research-pipeline/blob/main/archive/v3.0/celltrion-20260703.html) 샘플은 존재하지만 현재 데이터 계약으로 재검증되지 않은 v3.0 작업 기록이다. 현재 가상 예제는 실제 기업분석 근거로 사용하지 않았다. 완전 자동 수집·독립적 투자 가치 평가를 주장하지 않았다.

## 기존 디자인에서 바꾼 부분

기존 `content.json → build.py → docs/HTML·Markdown` 구조, 흰 배경·절제된 색상·목차·프로필 표·프로젝트 2열·명시적 인쇄 페이지 나눔을 재사용했다. 포인트 색상은 짙은 청록색으로 조정했다. 국내 주식 VFS 페이지를 제외하고 ETF 연구를 가장 앞에 배치했다. 나머지는 브리핑→운용 시스템→기업분석 순서다. 지원 조직과 영문 부제를 바꾸고 웹과 같은 HTML에서 PDF를 생성하는 스크립트를 추가했다. 기존 원격 저장소와 로컬 원본 파일은 수정하지 않았다.
