# My Skills Hub

Claude Code를 위한 커스텀 스킬 모음입니다. 개발 생산성을 높이기 위한 다양한 자동화 스킬들을 제공합니다.

## 스킬 목록

### 1. [Code Changelog](./skills/code-changelog/)
AI가 생성한 모든 코드 변경사항을 자동으로 문서화하고 웹 브라우저에서 실시간으로 확인할 수 있는 스킬입니다.

**주요 기능:**
- 자동 문서 생성 (Markdown)
- HTML 뷰어 (설치 불필요, Python 서버)
- 다크 모드 UI (GitHub 스타일)
- 실시간 서버 (http://localhost:4000)

**사용 시나리오:**
- 코드 리뷰 문서 자동 생성
- 변경 이력 추적
- 팀원과 변경사항 공유

### 2. [Meta Prompt Generator](./skills/meta-prompt-generator/)
간단한 설명을 받아 단계별 병렬 처리가 가능한 구조화된 커스텀 슬래시 커맨드를 자동으로 생성합니다.

**주요 기능:**
- 지능형 지식 수집 (웹 검색)
- 단계 기반 워크플로우 설계
- 포괄적인 테스트 생성
- 병렬 처리 최적화

**사용 시나리오:**
- 복잡한 프로젝트 워크플로우 자동화
- 재사용 가능한 슬래시 커맨드 생성
- 체계적인 테스트 스위트 작성

### 3. [Prompt Enhancer](./skills/prompt-enhancer/)
프로젝트 컨텍스트를 분석하여 간단한 개발 요청을 명확하고 상세한 요구사항으로 변환합니다.

**주요 기능:**
- 프로젝트 구조 자동 분석
- 기존 패턴 인식
- 구조화된 요구사항 생성
- 프레임워크별 최적화

**사용 시나리오:**
- "로그인 기능 만들어줘" → 상세한 구현 요구사항
- Clean Architecture 기반 설계 제안
- 프로젝트 컨벤션 자동 적용

**지원 스택:**
- Flutter (Clean Architecture, Riverpod)
- Next.js/React (App Router, Zustand)
- Python (Django, FastAPI)

### 4. [Flutter Init](./skills/flutter-init/)
도메인 기반 Flutter 프로젝트를 Clean Architecture로 자동 생성합니다.

**주요 기능:**
- 도메인 선택 (Todo/Habit/Note/Expense/Custom)
- 스택 프리셋 (Minimal/Essential/Full Stack/Custom)
- Clean Architecture 자동 생성
- Riverpod 3.0, Drift, Freezed 설정

**기술 스택:**
- Riverpod 3.x (상태 관리)
- Drift (로컬 데이터베이스)
- Freezed (불변 모델)
- Easy Localization (다국어)
- FluentUI Icons

**사용 시나리오:**
- 새로운 Flutter 앱 빠른 시작
- Clean Architecture 보일러플레이트
- 도메인 중심 설계

### 5. [Next.js 15 Init](./skills/nextjs15-init/)
도메인 기반 Next.js 15 프로젝트를 App Router로 자동 생성합니다.

**주요 기능:**
- 도메인 선택 (Todo/Blog/Dashboard/E-commerce/Custom)
- 스택 프리셋 (Minimal/Essential/Full Stack/Custom)
- App Router 기반 구조
- TypeScript Strict Mode

**기술 스택:**
- Next.js 15 (App Router)
- ShadCN/ui (UI 컴포넌트)
- Zustand (클라이언트 상태)
- Tanstack Query (서버 상태)
- Drizzle ORM (TypeScript ORM)
- Better Auth (인증)

**사용 시나리오:**
- 새로운 Next.js 앱 빠른 시작
- 타입 안전한 풀스택 앱
- 도메인 중심 설계

### 6. [Codex](./skills/codex/)
OpenAI Codex CLI를 사용하여 코드 분석, 리팩토링, 자동화된 편집을 수행합니다.

**주요 기능:**
- 대화형 모델 및 추론 레벨 선택 (gpt-5, gpt-5-codex)
- 샌드박스 모드 (read-only, workspace-write, danger-full-access)
- 세션 재개 기능 (codex exec resume --last)
- 자동화된 코드 편집 (--full-auto)

**사용 시나리오:**
- 코드 리뷰 및 분석
- 대규모 리팩토링 자동화
- 코드베이스 전체 수정 작업
- 이전 세션 이어서 작업

**샌드박스 모드:**
- `read-only`: 코드 분석 전용 (읽기만)
- `workspace-write`: 로컬 파일 수정
- `danger-full-access`: 네트워크 접근 포함 전체 권한

### 7. [Landing Page Guide](./skills/landing-page-guide/)
Next.js와 React로 고품질 전환율 높은 랜딩페이지를 제작하기 위한 종합 가이드입니다.

**주요 기능:**
- DESIGNNAS의 11가지 필수 요소 프레임워크 적용
- ShadCN UI 컴포넌트 통합
- SEO 최적화 및 접근성 표준 준수
- 반응형 디자인 및 성능 최적화

**11가지 필수 요소:**
1. 키워드가 포함된 URL
2. 회사 로고 (상단 왼쪽)
3. SEO 최적화된 제목과 부제목
4. 주요 CTA (히어로 섹션)
5. 사회적 증거 (리뷰, 통계)
6. 이미지 또는 동영상
7. 핵심 이점/기능 (3-6개)
8. 고객 후기 (4-6개)
9. FAQ 섹션 (5-10개 질문)
10. 최종 CTA (하단)
11. 연락처 정보 및 법적 페이지

**기술 스택:**
- Next.js 14+ (App Router)
- TypeScript
- Tailwind CSS
- ShadCN UI

**사용 시나리오:**
- 마케팅 랜딩 페이지 제작
- 제품 소개 페이지 개발
- 전환율 최적화가 필요한 프로모션 페이지
- SaaS/이커머스/서비스/이벤트 랜딩 페이지

### 8. [Card News Generator](./skills/card-news-generator/)
600x600 인스타그램 스타일 카드 뉴스 시리즈를 자동으로 생성합니다.

**주요 기능:**
- 주제와 색상만 입력하면 자동 생성
- 5-7장의 카드 시리즈 자동 제작
- 자동 텍스트 래핑 및 레이아웃
- RGB to Hex 색상 변환
- 단일 카드/멀티 카드 모드

**캔버스 사양:**
- 크기: 600x600 픽셀 (인스타그램 최적화)
- 자동 텍스트 줄바꿈
- 번호 배지, 제목, 본문 계층 구조
- 다양한 색상 프리셋 제공

**권장 색상:**
- 베이지: `245,243,238`
- 핑크: `255,229,229`
- 민트: `224,244,241`
- 라벤더: `232,224,245`
- 피치: `255,232,214`
- 스카이 블루: `227,242,253`

**사용 시나리오:**
- 소셜 미디어 카드 뉴스 제작
- 인스타그램 콘텐츠 시리즈
- 정보 전달용 카드 이미지
- 교육/마케팅 콘텐츠

## 스킬 사용 방법

### 설치

1. 스킬을 Claude Code 스킬 디렉토리로 복사:

```bash
# 유저 스킬로 설치 (전역)
cp -r skills/* ~/.claude/skills/

# 또는 프로젝트 스킬로 설치 (프로젝트별)
cp -r skills/* ./.claude/skills/
```

2. Claude Code에서 스킬 확인:

```
/skills
```

### 실행

각 스킬은 스킬 이름으로 실행할 수 있습니다:

```
code-changelog
meta-prompt-generator
prompt-enhancer
flutter-init
nextjs15-init
codex
landing-page-guide
card-news-generator
```

## 폴더 구조

```
my-skills-hub/
├── skills/
│   ├── code-changelog/          # 코드 변경사항 자동 문서화
│   │   ├── skill.md             # 스킬 설명
│   │   └── ...                  # 스킬 파일들
│   ├── meta-prompt-generator/   # 메타 프롬프트 생성기
│   │   ├── skill.md
│   │   └── ...
│   ├── prompt-enhancer/         # 프롬프트 향상기
│   │   ├── skill.md
│   │   └── ...
│   ├── flutter-init/            # Flutter 프로젝트 생성
│   │   ├── skill.md
│   │   └── ...
│   ├── nextjs15-init/           # Next.js 15 프로젝트 생성
│   │   ├── skill.md
│   │   └── ...
│   ├── codex/                   # Codex CLI 코드 리뷰/분석
│   │   └── skill.md
│   ├── landing-page-guide/      # 랜딩페이지 제작 가이드
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── 11-essential-elements.md
│   │       └── component-examples.md
│   └── card-news-generator/     # 카드 뉴스 자동 생성
│       ├── SKILL.md
│       └── ...
└── README.md                     # 이 파일
```

## 스킬별 상세 정보

각 스킬 폴더의 `skill.md` 파일에서 더 자세한 정보를 확인할 수 있습니다:

- [Code Changelog 상세 정보](./skills/code-changelog/skill.md)
- [Meta Prompt Generator 상세 정보](./skills/meta-prompt-generator/skill.md)
- [Prompt Enhancer 상세 정보](./skills/prompt-enhancer/skill.md)
- [Flutter Init 상세 정보](./skills/flutter-init/skill.md)
- [Next.js 15 Init 상세 정보](./skills/nextjs15-init/skill.md)
- [Codex 상세 정보](./skills/codex/skill.md)
- [Landing Page Guide 상세 정보](./skills/landing-page-guide/SKILL.md)
- [Card News Generator 상세 정보](./skills/card-news-generator/SKILL.md)

## 기여

새로운 스킬을 추가하거나 기존 스킬을 개선하고 싶으시다면:

1. `skills/` 폴더에 새로운 스킬 디렉토리 생성
2. `skill.md` 파일 작성 (스킬 메타데이터 및 설명)
3. 필요한 파일들 추가
4. README.md에 스킬 정보 추가

## 라이선스

MIT License

## 참고

이 스킬들은 Claude Code의 공식 문서를 참고하여 작성되었습니다:
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
