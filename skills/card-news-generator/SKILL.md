---
name: card-news-generator
description: Create 600x600 Instagram-style card news series automatically. User provides topic and colors, Claude generates content and creates multiple cards with proper text wrapping.
---

# Card News Generator - Auto Mode

Creates beautiful 600x600 card news series for social media. User only needs to provide topic and colors - Claude handles content generation and multi-card creation automatically.

## When to Use

Use this skill when user requests:
- "카드 뉴스 만들어줘"
- "주제로 카드 시리즈 만들어줘"
- "인스타용 카드 생성해줘"
- Any request for visual card content

## Core Workflow - AUTO MODE

This is the PRIMARY workflow when users request card news:

### Step 1: Get Topic and Colors from User

Ask user for:
- **Topic** (주제): What the card series is about
- **Background RGB** (배경색): e.g., `245,243,238` (optional, default: beige)

Example conversation:
```
Claude: 어떤 주제로 카드 뉴스를 만들까요?
User: Z세대의 특징에 대해서

Claude: 배경색을 선택해주세요 (RGB 형식, 예: 245,243,238)
추천 색상:
• 베이지: 245,243,238
• 핑크: 255,229,229
• 민트: 224,244,241
User: 245,243,238
```

### Step 2: Generate Card Content

Create 5-7 cards about the topic. Format output as:

```
1. [제목]
[설명 2-3줄]

2. [제목]
[설명 2-3줄]

3. [제목]
[설명 2-3줄]
```

**CRITICAL Content Guidelines:**
- **Title**: Maximum 20 characters (including spaces)
- **Content**: Maximum 60 characters (including spaces)
- Keep it concise to fit 600x600 canvas
- Use simple, impactful language
- Each card should convey ONE key point

### Step 3: Auto-Generate Cards

Use this command to create all cards at once:

```bash
python auto_generator.py \
  --topic "Z세대의 특징" \
  --bg-color "#f5f3ee" \
  --text-color "#1a1a1a" \
  --output-dir /mnt/user-data/outputs \
  --base-filename "zgen" << 'EOF'
1. 디지털 네이티브
태어날 때부터
디지털 환경에 익숙

2. 개인화 중시
나만의 개성과
취향을 중요시

3. 소통 방식
텍스트보다 영상
이모티콘으로 감정 표현
EOF
```

The script will automatically:
- Parse the numbered content
- Create individual cards with proper text wrapping
- Save as `zgen_01.png`, `zgen_02.png`, etc.

### Step 4: Provide Download Links

After generation, show user:
```
✅ 카드 뉴스 5장이 생성되었습니다!

[View card 1](computer:///mnt/user-data/outputs/zgen_01.png)
[View card 2](computer:///mnt/user-data/outputs/zgen_02.png)
...
```

## RGB to Hex Conversion

Always convert RGB to hex for scripts:

```python
# RGB 245,243,238 → Hex #f5f3ee
hex_color = '#{:02x}{:02x}{:02x}'.format(245, 243, 238)
```

## Recommended Colors (RGB Format)

Show users these options:
- Warm beige: `245,243,238` → `#f5f3ee`
- Soft pink: `255,229,229` → `#ffe5e5`
- Mint green: `224,244,241` → `#e0f4f1`
- Lavender: `232,224,245` → `#e8e0f5`
- Peach: `255,232,214` → `#ffe8d6`
- Sky blue: `227,242,253` → `#e3f2fd`

## Content Generation Best Practices

### Good Card Content Example
```
1. 디지털 네이티브
태어날 때부터
디지털 환경에 익숙
```
✓ Title: 8 characters
✓ Content: 18 characters
✓ Clear and concise

### Bad Card Content Example
```
1. Z세대는 디지털 네이티브 세대입니다
그들은 태어날 때부터 스마트폰과 인터넷을 사용하며 자랐기 때문에 디지털 기술에 매우 능숙합니다
```
✗ Title too long (21 characters)
✗ Content too long (60+ characters)
✗ Will overflow the 600x600 canvas

## Single Card Mode (Manual)

For creating just one card directly:

```bash
python generate_card.py \
  --title "제목" \
  --content "내용" \
  --bg-color "#f5f3ee" \
  --text-color "#1a1a1a" \
  --number 1 \
  --output /mnt/user-data/outputs/single.png
```

## Technical Details

### Canvas Specifications
- Size: 600x600 pixels (Instagram-optimized)
- Padding: 40px on all sides
- Max text width: 520px (600 - 80)
- Font sizes:
  - Number badge: 60px
  - Title: 48px (bold)
  - Content: 28px (regular)

### Text Wrapping
- Automatic word wrapping at max width
- Preserves manual line breaks
- Centers all text horizontally
- Vertical spacing optimized for readability

### File Naming Convention
- Auto mode: `{base_filename}_{number:02d}.png`
- Example: `card_01.png`, `card_02.png`, `card_03.png`

## Error Handling

If text overflows:
- Reduce title length
- Shorten content
- Use line breaks strategically
- Regenerate with revised content

## Example Workflow

User request: "Z세대에 대한 카드 뉴스 5장 만들어줘, 핑크색으로"

Claude response:
1. Confirm: "Z세대 특징에 대한 카드 5장을 핑크 배경(255,229,229)으로 만들겠습니다."
2. Generate 5 cards content (keeping text concise)
3. Run auto_generator.py with heredoc
4. Provide download links to all 5 cards

Total time: ~30 seconds for 5-card series
