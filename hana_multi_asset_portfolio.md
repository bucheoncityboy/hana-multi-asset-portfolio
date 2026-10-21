# 하나자산운용 지원 포트폴리오

**김재원 | 하나자산운용 글로벌멀티에셋운용본부 멀티에셋솔루션팀**

GLOBAL MULTI-ASSET RESEARCH & OPERATIONS SUPPORT

글로벌 금융시장 분석과 자산배분 / 포트폴리오 및 운용자료 관리 / 기업 리서치와 AI 활용

## 01. 학력

| 학교 | 전공 | 기간 | 비고 |
| --- | --- | --- | --- |
| 한양대학교(서울) | 경영학부 주전공 / 정보시스템학과 복수전공 | 2019.03~2026.08 | 졸업 |

## 02. 교내 활동

### GAMMA 글로벌마켓학회 | 2026.06~현재

- 일간 및 주간 글로벌 시장 브리핑 작성
- 해외 IB 리서치 분석 및 주요 시장 변화 정리
- 거시경제 분석과 한국은행 통화정책 이벤트 연구

### HY-FIN 재무금융학회 | 2025.09~2026.07

- Fama-French(1993) 재현 및 한국 시장 실증
- 환위험 관리 및 환헤지 연구 논문
- WorldQuant Brain 산학협력 활동

### Quantitative Analytics Lab (학부연구생) | 2025.09~2025.12

- 금융 머신러닝 및 Meta-Labeling 연구
- 금융 시계열 꼬리위험 정량화 및 리스크 관리

## 03. 자격증 및 수료

| 구분 | 내용 | 취득일 |
| --- | --- | --- |
| 자격증 | 투자자산운용사 (금융투자협회) | 2025.10.30 |
| 자격증 | SQL 개발자(SQLD) | 2024.04.05 |
| 자격증 | ADsP 데이터분석 준전문가 | 2024.05.31 |
| 수료 | Quantitative Research Consultant (WorldQuant) | 2026.06.04 |

## 04. 경력

**링커리어 현장실습 | 2024.09~2024.12**

- 실적 정산 및 보고서 작성
- 취업 콘텐츠 제작

## 05. 핵심 역량

- 글로벌 금융시장 리서치 및 자산배분 연구
- 포트폴리오 구축과 운용자료 관리
- AI 기반 데이터 검증 및 업무 자동화

---

## [2. 글로벌 ETF 자산배분 연구]

**프로젝트: Jump Model 및 경제 국면을 활용한 ETF 자산배분**

### 프로젝트 개요

시장 국면을 예측해 ETF 비중에 반영하고, 국면 정의와 예측모형에 따른 성과 차이를 검증했습니다.

시장 국면 분석 → 국면 예측 → ETF 비중 결정 → 성과 검증

- **수행 형태:** 개인 프로젝트 · 공개 ETF 응용 연구
- **수행 기간:** 2026.09
- **프로젝트 목표:** 경제 및 시장 국면의 차이가 자산배분에 주는 영향을 비교하고 투자 의사결정에 반영
- **검증 범위:** F141: 2014.01~2025.09, 141개월 · ETF 8종과 BIL · 편도 거래비용 5bp

### 데이터 및 설계

- SPY·EFA·EEM(주식), IEF·TLT·LQD(채권), IYR(부동산), GLD(금)와 현금성 ETF BIL을 활용
- Jump Model로 자산별 강세·약세를 추정하고, 산업생산과 물가 모멘텀의 방향으로 경제 4국면 구성
- Yahoo ETF 가격, ALFRED 경제 빈티지와 FRED 시장자료를 수집하고 이용 가능 시점 반영

### 주요 수행 내용

- 과거 5년 학습·3년 순차 검증 후 6개월마다 재학습하고, 예측한 국면을 목표 비중에 반영
- 종가 후 판단·다음 거래일 시가 체결과 거래비용을 반영해 동일 배분 조건에서 모형별 성과 비교

**141개월 | F141 · 2014.01~2025.09 · 비용 차감 연구 결과**

국면 정의와 예측모형별 연 CER

| 국면 정의 | 예측모형 | 연 CER |
| --- | --- | --- |
| 자산 2국면 | 로지스틱 | 2.11% |
| 자산 2국면 | XGBoost | 2.69% |
| 경제 4국면 | 로지스틱 | 6.62% |
| 경제 4국면 | XGBoost | 5.90% |

CER: 수익과 위험을 함께 반영한 지표. 월 순수익·위험회피계수 5 기준이며 연 수익률과 구분합니다.

### 검증 결과 및 성과

- 경제 4국면 XGBoost의 CER가 자산 2국면보다 3.21%p 높음. 두 국면 모두 XGBoost의 로지스틱 대비 통계적 우위는 미확인
- 기준 전략 CER: 국면 없는 평균분산 4.69%, SPY/IEF 60/40 7.00%. 모든 비교군을 앞서지는 못함

> 과거 결과를 본 뒤 설계한 역사적 연구로, 원 논문의 동일자료 재현이나 전향 검증이 아닙니다. 시장자료의 과거 수정 이력은 완전히 복원하지 못했습니다. 별도 12 ETF·117개월 후속 연구와 자료·설계가 다릅니다.

### 관련 자료

- [GitHub 저장소](https://github.com/bucheoncityboy/korean-macro-factor-allocation)
- [F141 전체 결과·한계](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/docs/followup.md)
- [F141 성과 원자료](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/results/followup/summary.csv)
- [비용 차감 NAV·낙폭](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/results/followup/figures/long_nav.png)
- [데이터 출처·시점](https://github.com/bucheoncityboy/korean-macro-factor-allocation/blob/main/docs/data.md)
- [별도 후속 연구(117개월)](https://github.com/bucheoncityboy/global-etf-regime-allocation)

---

## [3. 글로벌 시장 브리핑 AI 자동화]

**프로젝트: Multi-Asset Morning Briefing**

### 프로젝트 개요

공식 시장자료의 수집과 기준일 검증을 자동화해 운용부서에서 활용할 브리핑 작성 절차를 구현했습니다.

- **수행 형태:** 글로벌마켓학회 활용 및 K-Skill 오픈소스 기여
- **수행 기간:** 2026.09
- **프로젝트 목표:** 미국·한국 시장자료의 기준일과 수치를 확인하고 출처가 남는 글로벌 브리핑 작성
- **검증 범위:** 작성시간 단축은 학회원 사용 피드백 기준. 독립적인 업무시간 측정 실험과 구분

### 데이터 및 설계

- 미국 재무부 국채금리, Cboe VIX, ECB 환율과 한국은행 ECOS를 활용. FRED는 발표 지연을 확인하는 보조 원천으로 사용
- 미국·한국의 거래일과 휴장일, 제공기관별 업데이트 시점을 구분하고 관측일·단위가 맞는 값만 반영
- 주식·금리·외환·원자재·변동성을 연결하고 한국시장 영향과 주요 일정을 포함한 7개 영역으로 구성

### 주요 수행 내용

- 공식 CSV·API 응답을 수집하고 값·단위·기준일을 점검하는 Python 스크립트 개발
- 발표 지연과 기준일 불일치가 있는 값은 제외하고, 출처와 관측일을 남겨 AI가 브리핑을 작성하도록 구성
- 학회원 피드백을 받아 반복 확인과 자료 정리 과정을 개선

**40분 → 10분 이내 | 브리핑 작성시간 · 학회원 사용 피드백 기준**


### 검증 결과 및 성과

- 학회원 사용 피드백 기준 작성시간 약 40분에서 10분 이내로 단축
- K-Skill 정식 기능 채택(PR #675, 2026.09.19 병합)
- 기업분석·시장 이벤트·한미 국채·한국 채권 조회를 포함한 금융 리서치 AI 스킬 5종의 PR 병합에 기여

> 작성시간은 학회원의 사용 피드백이며 별도의 통제 실험 결과가 아닙니다. 스킬 5종의 기여는 공개 PR 병합 기록으로 확인했습니다.

### 관련 자료

- [GitHub 저장소](https://github.com/bucheoncityboy/multi-asset-morning-briefing)
- [스킬과 검증 규칙](https://github.com/bucheoncityboy/multi-asset-morning-briefing/blob/main/README.md)
- [PR #675](https://github.com/NomaDamas/k-skill/pull/675)
- [PR #682](https://github.com/NomaDamas/k-skill/pull/682)
- [PR #683](https://github.com/NomaDamas/k-skill/pull/683)
- [PR #684](https://github.com/NomaDamas/k-skill/pull/684)
- [PR #685](https://github.com/NomaDamas/k-skill/pull/685)

---

## [4. 미국 대형주 전략 및 운용 시스템]

**프로젝트: 미국 대형주 팩터 전략 및 운용 시스템 구축**

### 프로젝트 개요

전략 검증부터 목표 비중 산출과 보유분 대조, 주문자료 작성 및 Excel 원장 관리까지 연결했습니다.

- **수행 형태:** 개인 프로젝트
- **수행 기간:** 2026.06 ~ 2026.08
- **프로젝트 목표:** 미국 대형주 팩터 전략의 투자 신호를 정확한 목표 비중과 주문자료·원장으로 연결
- **검증 범위:** 개인 프로젝트의 코드와 로컬 주문 상태·Excel 실행결과표 대조. 실제 브로커 체결의 독립 검증과 구분

### 데이터 및 설계

- 현재 S&P500 구성종목의 유동성을 기준으로 최대 150종 투자 유니버스 구성. 과거 구성종목을 복원한 자료는 아님
- Leader 60%, 63거래일 모멘텀 20%, 저변동성 20%로 구성하고 종목별 합산 비중을 15%로 제한
- 월말 신호를 확정해 다음 거래일 시가에 리밸런싱하는 규칙 적용

### 주요 수행 내용

- 과거 학습 구간에서 후보를 선택하고 이후 6개월씩 5개 구간에서 평가하는 Walk-Forward 검증 절차 구현
- 보유 수량과 목표 비중을 비교해 매도 우선 주문자료를 만들고 가격·수량 누락, 현금 부족과 중복 실행 점검
- 브로커 주문의 체결 상태를 점검하고 Excel 원장의 주문 상태에 반영하는 경로 구현. 보유분·선정 종목·주문자료 등 7개 시트 연계

**150종목 / 7개 시트 | 투자 유니버스와 Excel 원장 구성**


### 검증 결과 및 성과

- 투자 신호 → 목표 비중 → 주문자료 → Excel 원장으로 이어지는 운용자료 관리 절차 구현
- 연구·운용 종목 자격 불일치와 주문 누락 등 9개 결함 수정 기록 확인
- 로컬 로그의 매수 29건·매도 1건을 Excel 실행결과표와 대조해 상태·수량·평균가 일치 확인

> 로그와 원장은 같은 애플리케이션에서 생성한 기록입니다. 브로커 원본과의 대조 및 매도 29건은 확인하지 못했습니다. 기관 펀드 운용 경험과 실계좌 수익률 검증으로 확대하지 않습니다.

### 관련 자료

- [GitHub 저장소](https://github.com/bucheoncityboy/us-robust-live-ops)
- [Excel 원장 생성·7개 시트](https://github.com/bucheoncityboy/us-robust-live-ops/blob/main/ops/ops_excel_write.py)
- [9개 결함 수정 기록](https://github.com/bucheoncityboy/us-robust-live-ops/blob/main/docs/audit_fixes.md)
- [주문 전 검증 코드](https://github.com/bucheoncityboy/us-robust-live-ops/blob/main/ops/ops_execute_gates.py)

---

## [5. 기업분석 AI 에이전트]

**프로젝트: 기업분석 AI 에이전트 및 리서치 파이프라인**

### 프로젝트 개요

기업 공시와 실적자료의 수치를 대조하고 분석 쟁점과 출처를 정리하는 리서치 보조 절차를 구현했습니다.

- **수행 형태:** 개인 프로젝트
- **수행 기간:** 2026.05
- **프로젝트 목표:** 기업 및 산업 리서치에 필요한 자료 수집·수치 대조·보고서 작성을 지원
- **검증 범위:** 자료 대조 및 보고서 작성 기능과 공개 샘플 확인. 확인되지 않은 수치는 임의로 채우지 않도록 설계

### 데이터 및 설계

- 기업 공시·IR·실적발표 자료를 우선 조사하고, 컨센서스와 시장자료를 참고해 실적과 산업 쟁점 정리
- 원문 수치와 분석에 사용한 값의 출처·수집일을 기록하고 재무제표의 기간·단위를 구분
- 자료 조사와 해석은 에이전트가, 계산과 출력 검증은 도구가 맡도록 절차 구성

### 주요 수행 내용

- 공시와 실적발표의 주요 재무 수치를 대조하고 차이가 있으면 근거와 확인 필요 사항 기록
- 확인되지 않은 수치를 임의로 채우지 않고 미확인 상태로 표시하는 검증 절차 구현
- 분석 결과와 출처를 보고서로 작성하고 실제 기업분석 샘플의 자료·출력 흐름 확인

**공시 ↔ 실적발표 | 주요 수치 대조 후 핵심 쟁점과 근거 정리**


### 검증 결과 및 성과

- 공시·실적자료 대조와 출처 기록을 포함한 기업 리서치 보조 파이프라인 구축
- 두산에너빌리티·셀트리온의 공개 보고서 샘플 확인(문서 표기일 2026.07.03, v3.0)
- 현재 v3.2 스킬의 자료 수집·계산·보고서 검수 절차를 저장소에 공개

> 공개 실제 보고서는 현재 계약으로 재검증하지 않은 v3.0 자료입니다. 현재 실행 예제는 가상 수치이며 실제 분석 근거로 사용하지 않습니다. 자료 수집·대조·보고서 작성 절차를 확인한 범위입니다.

### 관련 자료

- [GitHub 저장소](https://github.com/bucheoncityboy/agentic-research-pipeline)
- [현재 스킬과 검증 절차](https://github.com/bucheoncityboy/agentic-research-pipeline/blob/main/README.md)
- [두산에너빌리티 보고서](https://bucheoncityboy.github.io/hana-multi-asset-portfolio/reports/doosan-enerbility-20260703.pdf)
- [셀트리온 보고서](https://bucheoncityboy.github.io/hana-multi-asset-portfolio/reports/celltrion-20260703.pdf)

