# 출처 대조와 편집 판단

최초 확인일: 2026-10-21 / 최종 대조일: 2026-10-22 (한국시간)

## 지원 직무

[인턴 공식 공고](https://www.kofia.or.kr/brd/m_96/view.do?seq=42668)의 글로벌 경제·기업/산업·금융시장 리서치 지원, 글로벌 펀드 운용 보조를 기준으로 구성했다. [동일 팀 경력직 공고](https://www.kofia.or.kr/brd/m_96/view.do?seq=40642)의 글로벌 자산배분 EMP 및 해외 펀드 관련 업무는 팀의 업무 배경을 이해하는 데만 참고했다. 펀드 설정·환매·F/X·기관 RFP를 인턴 확정 업무나 지원자의 수행 경력으로 기재하지 않았다. Bloomberg 활용 경험과 영어 능력은 새로 추정해 추가하지 않았다.

## 프로필과 문체

기존 포트폴리오 `content.json`의 학력·학회·자격·수료·링커리어 경험을 재사용했다. 로컬의 기존 자소서 아카이브 PDF 34~38페이지와 수행 내용·문장 구조를 대조했다. 2026.09 ETF 연구 기간, 브리핑의 사용 피드백, 개인 운용과 코드 검증의 구분을 유지했다. 연락처·생년월일·주소 등은 공개 파일에 추가하지 않았다. 개인 원문은 이 저장소에 포함하지 않는다.

2026.10.22 사용자의 브라우저 코멘트에 따라 `실무 경험`을 `경력`으로 바꾸고 링커리어 수행 내용을 `실적 정산 및 보고서 작성 / 취업 콘텐츠 제작`으로 교체했다. 기존 정산 오류 0건 문구도 이 교체 범위에서 삭제했다. 이름은 프로필 본문에 유지하고 목차의 반복 이름을 `PORTFOLIO`로 교체했다. 나머지 레이아웃·색상·서체·프로젝트 순서는 유지했다.

## ETF 자산배분

- [README](https://github.com/bucheoncityboy/korean-macro-factor-allocation), [F141 CSV](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/results/followup/summary.csv), [전체 결과](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/docs/followup.md), [데이터 명세](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/docs/data.md)를 대조했다.
- CSV에서 `cohort=long`, `policy=primary`, `cost_bp=5`, `months=141`로 필터링하고 네 예측 조합과 두 기준 전략의 CER를 대조했다. 기간은 2014.01~2025.09, 위험자산은 8 ETF와 현금 BIL이다.
- 연 CER는 자산2 로지스틱 2.11%, 자산2 XGBoost 2.69%, 경제4 로지스틱 6.62%, 경제4 XGBoost 5.90%다. 경제4 XGBoost와 자산2 XGBoost의 차이는 3.21%p이나 국면 정의·표적이 다른 비교다. 두 국면 모두 XGBoost의 로지스틱 대비 통계적 우위는 확인되지 않았다.
- 같은 CSV 조건에서 국면 없는 평균분산 `unconditional_mv`의 연 CER는 4.69%, `spy_ief_60_40`은 7.00%다. 동일 평가기간·거래비용·월 순수익 CER(위험회피계수 5) 기준의 비교이며, 각 전략의 배분 규칙까지 같다는 뜻은 아니다. 경제4의 국면 정의 효과를 관찰했지만 국면 예측 전략이 모든 비교군을 앞선 것은 아니라는 설명을 본문에 보완했다. CAGR 열은 CER와 구분했다.
- 일반 수익률로 오해하지 않도록 CER를 정의했다. 원문 동일자료 재현·전향 검증으로 표현하지 않았다. 시장자료의 과거 수정 빈티지 복원 한계를 명시했다.
- F141 비교표가 5페이지 보고서에서 읽기 쉬워 본문에 사용하고 기존 NAV·낙폭 차트는 증빙 링크로 연결했다. [별도 후속 저장소](https://github.com/bucheoncityboy/global-etf-regime-allocation)의 12 ETF·117개월 결과는 본문 수치에 혼합하지 않았다.

## 글로벌 브리핑

[README](https://github.com/bucheoncityboy/multi-asset-morning-briefing), `scripts/market_data.py`, 테스트와 규칙 문서를 확인했다. 미국 재무부·Cboe·ECB·ECOS를 우선 사용하며 FRED는 지연을 확인하는 보조 원천이다. 약 40분→10분 이내는 자소서·사용자 제공 내용의 학회원 피드백으로 통제 실험이 아니다.

K-Skill PR [675](https://github.com/NomaDamas/k-skill/pull/675), [682](https://github.com/NomaDamas/k-skill/pull/682), [683](https://github.com/NomaDamas/k-skill/pull/683), [684](https://github.com/NomaDamas/k-skill/pull/684), [685](https://github.com/NomaDamas/k-skill/pull/685)의 작성자와 `merged_at`을 API로 대조했다. 브리핑은 2026.09.19, 나머지 네 PR은 2026.09.30에 병합됐다. 정식 기능 채택·금융 리서치 스킬 5종 기여 표현은 이 기록에 한정한다.

## 미국 대형주 운용자료

[최신 README](https://github.com/bucheoncityboy/us-robust-live-ops), 공통 정책·주문 검증·Excel 생성 코드와 [9개 결함 수정 기록](https://github.com/bucheoncityboy/us-robust-live-ops/blob/main/docs/audit_fixes.md)을 확인했다. 공개 Excel 템플릿 자체는 6개 시트이며 현재 `ops/ops_excel_write.py`가 `06_Weekly_Trend`를 추가해 7개 시트를 구성하는 경로를 확인했다. 7개 시트는 현재 코드 구성에 대한 표현이며 템플릿 파일의 시트 수와 구분한다. 포트폴리오 증빙 링크도 현재 생성 코드로 연결했다. WFA 구현과 과거 시장 성과 재산출의 한계를 구분하고 구형/수정 전 백테스트 수익률은 포트폴리오에서 제외했다.

공개 저장소는 실제 브로커 체결과 실계좌 수익률을 미검증으로 표시한다. 최종 검수에서 로컬 JSONL 실행 로그 6개와 실행 요약·상태 파일, 6~8월 Excel 원장을 읽기 전용으로 확인했다. 로그의 `FILL / FILLED / FULL_FILL` 기록은 매수 29건·매도 1건이고, 비어 있지 않은 고유 주문 식별자 30개를 기준으로 중복은 0건이었다. 이것은 주문 상태 기록 수이며 브로커가 제공한 개별 체결 내역의 건수와 같다고 단정하지 않는다.

8월 원장 `05_Trade`의 주문 예정표에는 매수 29개 행이 `FILLED`로 표시되어 있고 예정 수량이 로그의 요청 수량과 일치한다. 같은 시트의 별도 실행결과표 30개 행은 로그의 종목·방향·상태·실제 기록 수량·평균가·주문 및 클라이언트 식별자와 모두 일치했다. 예정 수량과 실행 수량을 혼동하지 않았고, 금액 기준 매수의 추정 수량과 실제 기록 수량 차이를 미체결로 해석하지 않았다. 이 내부 대조 범위를 포트폴리오에 반영했다.

`execute_attempt_result.json`의 `DONE / http_order_posts=29`는 애플리케이션 실행 요약이다. `execute_status.json`의 30개 항목은 종목별 상태 병합 결과여서 매수·매도 건수를 따로 입증하지 못한다. 브로커 원본 응답·거래명세와의 독립 대조, 매도 29건, 계좌 현금흐름·손익 일치는 확인하지 못했다. 로그와 Excel은 같은 시스템에서 생성되어 서로 일치해도 독립적인 실제 체결 검증은 아니다. 원본·계좌번호·주문 식별자·인증정보는 공개하지 않았고 실제 주문이나 브로커 API 호출도 하지 않았다. 공개 기록에는 집계 수와 대조 항목만 남겼다.

## 기업 리서치

[현재 README](https://github.com/bucheoncityboy/agentic-research-pipeline)와 v3.2 코드, 기본 브랜치 전체 이력 및 공개 보조 브랜치를 확인했다. [2026.08.31의 v3.0 README](https://github.com/bucheoncityboy/agentic-research-pipeline/blob/fa47627a735816032631ff8f17b6281aadeb5a59/README.md)는 서로 다른 19개 기업을 커버리지로 명시한다. 이는 당시 문서의 목록으로 확인되며 19개 종목별 지원 구현·성공 검증이나 전체 분석 완료를 입증하는 기록과는 구분한다. 공개 구버전 산출물에는 서로 다른 기업 5개의 샘플이 있으며 중복 HTML/PDF를 추가 기업으로 집계하지 않았다. 이것이 실제로 분석한 기업의 전체 수라는 뜻도 아니다. 최신 배포본에는 고정 19종목 등록·지원 목록이 없으므로 수치를 본문에 복원하지 않았다.

[두산에너빌리티](https://github.com/bucheoncityboy/agentic-research-pipeline/blob/main/archive/v3.0/doosan-enerbility-20260703.html)와 [셀트리온](https://github.com/bucheoncityboy/agentic-research-pipeline/blob/main/archive/v3.0/celltrion-20260703.html)은 문서에 `GJC Pipeline v3.0 / 2026-07-03`이 표시되어 있고, [2026.07.10 최초 공개 커밋](https://github.com/bucheoncityboy/agentic-research-pipeline/tree/ec409eb60d65d8e7e67ac48f2b220c0c7d0f8529/examples)에 존재한다. 7월 3일은 문서 표기일이며 생성 프로그램의 독립 실행 시각을 입증하는 로그는 아니다. 현재 계약으로 재검증되지 않은 v3.0 기록이라는 설명을 유지하고 본문에 날짜·버전을 추가했다. 현재 가상 예제는 실제 분석 근거로 사용하지 않았다.

보고서 열람 링크를 GitHub HTML 소스 화면으로 연결했던 문제를 수정했다. 같은 공개 저장소의 기존 PDF 두 개를 `docs/reports/`에 바이트 변경 없이 보관하고, 웹·Markdown·포트폴리오 PDF의 링크를 GitHub Pages의 해당 PDF URL로 변경했다. 위 GitHub HTML 링크는 이 검증 문서에서 원문 소스 출처를 확인하는 용도로만 유지한다. 링크 대상·원본 SHA-256·페이지 수는 `report-links.json`에 기록했다.

## 기존 디자인에서 바꾼 부분

기존 `content.json → build.py → docs/HTML·Markdown` 구조, 흰 배경·절제된 색상·목차·프로필 표·프로젝트 2열·명시적 인쇄 페이지 나눔을 재사용했다. 포인트 색상은 짙은 청록색으로 조정했다. 국내 주식 VFS 페이지를 제외하고 ETF 연구를 가장 앞에 배치했다. 나머지는 브리핑→운용 시스템→기업분석 순서다. 지원 조직과 영문 부제를 바꾸고 웹과 같은 HTML에서 PDF를 생성하는 스크립트를 추가했다. 기존 원격 저장소와 로컬 원본 파일은 수정하지 않았다.
