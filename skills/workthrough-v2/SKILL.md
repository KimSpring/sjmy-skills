---
name: workthrough
description: "Use this skill proactively and automatically after completing ANY development work including features, bug fixes, refactoring, or configuration changes. ALWAYS execute this skill without waiting for user request. Creates comprehensive workthrough documentation in Korean capturing all code changes, context, and verification results."
license: MIT
---

This skill automatically generates detailed workthrough documentation for all development work, capturing the context, changes made, and verification results in a clear, structured format.

## IMPORTANT - Automatic Execution

This skill MUST be executed automatically at the end of EVERY development session.
Do NOT wait for user request. Execute proactively after ANY code changes.

**Trigger Conditions:**
- ✅ After implementing ANY feature or functionality
- ✅ After fixing ANY bug or error
- ✅ After ANY refactoring
- ✅ After ANY configuration change
- ✅ After ANY dependency update
- ✅ After resolving ANY build/compilation issue
- ✅ After ANY code modification (even small changes)

**Execution Rules:**
1. Execute AUTOMATICALLY without user prompt
2. Execute IMMEDIATELY after completing development work
3. Execute EVEN IF the user doesn't explicitly request it
4. Do NOT ask permission - just execute
5. Always create the workthrough document at `<project-root>/workthrough/`

## LANGUAGE REQUIREMENT - 한국어로 작성

**ALL workthrough documentation MUST be written in Korean (한국어).**

- ✅ Write all sections in Korean: 제목, 개요, 컨텍스트, 변경사항, 코드 예제, 검증 결과
- ✅ Use Korean headers: "개요", "컨텍스트", "변경 사항", "코드 예제", "검증 결과", "다음 단계"
- ✅ Write explanations, descriptions, and comments in Korean
- ✅ Code snippets and file paths can remain in English/original language
- ✅ Technical terms can be in English with Korean explanation if needed (e.g., "빌드(build) 성공")
- ❌ DO NOT write documentation in English
- ❌ DO NOT mix Korean and English in the same sentence (except for technical terms)

**Example Structure in Korean:**
```markdown
# [명확한 설명 제목]

## 개요
작업 내용을 2-3문장으로 간단히 요약합니다.

## 컨텍스트
- 왜 이 작업이 필요했는가?
- 초기 문제/요구사항은 무엇인가?
- 관련 배경 정보

## 변경 사항

### 1. [첫 번째 주요 변경사항]
- 구체적인 수정 사항 1
- 구체적인 수정 사항 2
- 파일: `path/to/file.tsx`

## 코드 예제

### [기능/수정 이름]
```typescript
// src/path/to/file.tsx
const example = () => {
  // 주요 코드 변경사항 표시
}
```

## 검증 결과

### 빌드 검증
```bash
> 빌드 명령어 출력
✓ 컴파일 성공
종료 코드: 0
```

## 다음 단계
- 필요한 후속 작업
- 알려진 제한사항 또는 향후 개선사항
```

## When to Use This Skill

Use this skill automatically after:
- Implementing new features or functionality
- Fixing bugs or errors
- Refactoring code
- Making configuration changes
- Updating dependencies
- Resolving build/compilation issues
- Any significant code modifications

## Documentation Structure

The workthrough documentation follows this structure:

1. **Title**: Clear, descriptive title of the work completed
2. **Overview**: Brief summary of what was accomplished and why
3. **Changes Made**: Detailed breakdown of all modifications
4. **Code Examples**: Key code snippets showing important changes
5. **Verification Results**: Build/test results confirming success

## Implementation Guidelines

When generating workthrough documentation:

### 1. Capture Complete Context
- What problem was being solved?
- What errors or issues existed before?
- What approach was taken?
- Why were specific decisions made?

### 2. Document All Changes Systematically
- List each file modified with full paths
- Describe what changed in each file
- Include before/after code snippets for significant changes
- Note any dependencies added or removed
- Document configuration updates

### 3. Show Code Examples
Use clear, well-formatted code blocks:
```language
// file: src/path/to/file.tsx
<div className="example">
  {/* Show relevant code changes */}
</div>
```

### 4. Include Verification
- Build output showing success
- Test results
- Error messages (if any remain)
- Exit codes
- Screenshots (if relevant)

### 5. Use Clear Formatting
- Use markdown headers (##, ###)
- Use bullet points and numbered lists
- Use code blocks with syntax highlighting
- Use blockquotes for output/logs
- Keep paragraphs concise

## Document Organization

Save workthrough documents with this naming convention at the project root:
```
<project-root>/workthrough/YYYY-MM-DD_HH_MM_brief-description.md
```

Example locations:
```
/Users/username/project/workthrough/2025-11-19_14_12_feature-implementation.md
/path/to/project/workthrough/2025-11-19_15_30_bug-fix.md
```

Optional: Organize by subdirectories if needed:
```
<project-root>/workthrough/features/2025-11-19_14_12_new-feature.md
<project-root>/workthrough/bugfixes/2025-11-19_15_30_issue-123.md
```

## Example Workthrough Structure

```markdown
# [Clear Descriptive Title]

## Overview
Brief 2-3 sentence summary of what was accomplished.

## Context
- Why was this work needed?
- What was the initial problem/requirement?
- Any relevant background information

## Changes Made

### 1. [First Major Change]
- Specific modification 1
- Specific modification 2
- File: `path/to/file.tsx`

### 2. [Second Major Change]
- Specific modification 1
- File: `path/to/another-file.ts`

### 3. [Additional Changes]
- Dependencies added: `package-name@version`
- Configuration updates: `config-file.json`

## Code Examples

### [Feature/Fix Name]
```typescript
// src/path/to/file.tsx
const example = () => {
  // Show the key code changes
}
```

## Verification Results

### Build Verification
```bash
> build command output
✓ Compiled successfully
Exit code: 0
```

### Test Results
```bash
> test command output
All tests passed
```

## Next Steps
- Any follow-up tasks needed
- Known limitations or future improvements
```

## Automation Instructions

After completing ANY development work:

1. **Determine Project Root**
   - Find the project root directory (containing .git, package.json, pubspec.yaml, etc.)
   - This is where the workthrough folder will be created

2. **Gather Information**
   - Review all files modified during the session
   - Collect build/test output
   - Identify the main objective that was accomplished

3. **Create Document**
   - Generate workthrough document in `<project-root>/workthrough/` directory
   - Use timestamp format: YYYY-MM-DD_HH_MM_brief-description.md
   - Follow the structure guidelines above

4. **Be Comprehensive**
   - Include all relevant details
   - Don't assume future readers have context
   - Document decisions and reasoning
   - Show concrete examples

5. **Verify Completeness**
   - Confirm all changes are documented
   - Include verification results
   - Add any relevant warnings or notes

6. **Build VitePress Documentation**
   - After creating the workthrough document, automatically build the VitePress site
   - Navigate to the workthrough directory: `cd <project-root>/workthrough`
   - Run the build command: `npm run build`
   - This ensures the documentation site is always up-to-date
   - If npm dependencies are not installed, skip the build step and notify the user

## Quality Standards

Good workthrough documentation should:
- Be readable by other developers
- Provide enough detail to understand changes
- Include verification that changes work
- Serve as a reference for similar future work
- Capture important decisions and context

Avoid:
- Overly verbose descriptions
- Unnecessary technical jargon
- Missing verification steps
- Vague or unclear explanations
- Incomplete code examples

## Output Location

IMPORTANT: Always save workthrough documents to the project root directory:
```
<project-root>/workthrough/YYYY-MM-DD_HH_MM_brief-description.md
```

- Determine the project root by finding the nearest `.git` directory or common project markers (package.json, pubspec.yaml, etc.)
- Create the `workthrough/` directory at the project root if it doesn't exist
- Do NOT create workthrough folders in subdirectories or nested project folders

## Integration with Workflow

This skill should be triggered automatically at the end of development sessions. The documentation serves as:
- A development log/journal
- Knowledge base for the project
- Onboarding material for new developers
- Reference for debugging similar issues
- Record of architectural decisions

## VitePress Integration

This workthrough documentation is integrated with VitePress for easy browsing:

1. **Automatic Sidebar**: New workthrough documents are automatically added to the sidebar
2. **Search Functionality**: All documents are searchable via the built-in search
3. **Auto-Build**: After creating a document, the VitePress site is automatically built
4. **View Documentation**: Run `npm run dev` in the workthrough folder to view the site locally

### Build Process

After each workthrough document is created:
```bash
cd <project-root>/workthrough
npm run build
```

The build creates a static site in `.vitepress/dist/` that can be:
- Deployed to any static hosting (Vercel, Netlify, GitHub Pages, etc.)
- Viewed locally with `npm run preview`
- Shared with team members for easy documentation browsing

Remember: Good documentation is a gift to your future self and your team.
