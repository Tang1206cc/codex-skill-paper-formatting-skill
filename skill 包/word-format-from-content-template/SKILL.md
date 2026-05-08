---
name: word-format-from-content-template
description: Format Word documents from user-provided content, formatting specifications, and Word templates while preserving the draft text exactly. Use when the user provides or references a 格式规范文件, 原始稿件, Word模板, .doc/.docx template, school/company document standard, thesis/report formatting rules, or asks Codex to 按规范排版 Word 文件, 套模板, 严格排版, 保持内容不变, or perform DOCX layout production without rewriting the supplied content.
---

# Word Format From Content Template

## Non-Negotiables

- Read the full formatting specification before writing the final document.
- Preserve the user-provided draft content exactly. Do not polish, summarize, expand, translate, delete, or rewrite content unless the user explicitly asks for content editing.
- Treat the Word template as a layout carrier. Remove or replace template sample text so it cannot leak into the final document.
- Convert every applicable rule in the specification into a checkable formatting checklist before final delivery.
- Verify both dimensions before delivery: the output follows the specification, and the output contains the user's original content with no unintended text changes.
- Render the final DOCX to visual pages when tooling permits. Inspect pages for clipping, overlap, table breaks, missing headers/footers, bad page numbers, and stale fields.

## 中文硬性契约

- 必须先完整阅读规范文件，建立完整排版和写入思路，再开始写入模板。
- 内容不得改写：原稿件的正文、标题、表格文字、注释、参考文献等均不得润色、删减、扩写、换写或自行补充。
- 只允许处理排版层事项，包括样式、段落、页边距、页眉页脚、页码、目录、题注、表格版式、分页和字段更新。
- 模板旧内容不得混入最终稿；所有示例文字、占位文字、旧题目、旧作者信息和旧正文都要清理或替换。
- 每条规范都要形成可执行清单，并在交付前逐条自查。
- 必须完成内容一致性检查和渲染视觉检查；若工具失败，要说明失败原因并采用可行替代检查。

## Workflow

1. **Collect and identify inputs**
   - Identify the formatting specification file, source draft file, and Word template file.
   - If multiple candidates exist, inspect filenames and nearby context before asking.
   - Preserve original files; create a clearly named output file.

2. **Extract source truth**
   - Read the full specification with suitable tools: `textutil` for `.doc/.docx` on macOS, PDF extraction/rendering for PDFs, and OOXML inspection when formatting details matter.
   - Extract the draft content separately and mark it as immutable content.
   - Inspect the template for reusable styles, page setup, headers, footers, cover blocks, sample text, fields, and section breaks.

3. **Build the formatting contract**
   - Write a concise checklist covering page setup, margins, fonts, line spacing, paragraph indents, heading hierarchy, page breaks, headers/footers, page numbering, TOC behavior, tables, figures, captions, footnotes, references, appendices, and any school/company-specific rules.
   - Decide which parts are copied from the template and which are reconstructed through explicit DOCX styles or OOXML.

4. **Format without rewriting**
   - Insert the draft content into the template structure.
   - Apply styles, numbering, tables, captions, page breaks, sections, headers/footers, and fields according to the checklist.
   - Keep content changes limited to mechanical layout needs such as paragraph splitting, heading style assignment, whitespace normalization required by Word, and field generation.

5. **Verify**
   - Run a content-consistency check between extracted draft text and final text.
   - Search final text for template residue and unrelated old sample content.
   - Render pages with the Documents skill renderer or LibreOffice/`soffice`; if rendering fails, use the best available fallback and disclose the limitation.
   - Iterate until both the formatting checklist and content-consistency checklist pass.

See `references/workflow.md` for the detailed operating procedure and `references/quality-checklists.md` for reusable QA checklists. Use `scripts/compare_text.py` to support source-vs-final text comparison.

## Tool Guidance

- Prefer the existing Documents skill for `.docx` creation, editing, and render-to-PNG verification.
- Use `python-docx` for deterministic style, paragraph, table, header/footer, and section work when it is sufficient.
- Use OOXML inspection or patching when field codes, numbering definitions, page numbering, section properties, or table geometry cannot be controlled reliably through high-level APIs.
- On macOS, `textutil -convert txt -stdout <file>` is a practical first pass for `.doc` and `.docx` text extraction.
- Use LibreOffice/`soffice` conversion plus page PNG inspection for final visual QA. If Chinese or spaced paths cause conversion issues, copy the DOCX to a temporary ASCII path for rendering only, leaving the final deliverable path unchanged.

## Delivery Standard

Return the final Word file path and briefly state:

- which specification/template/draft were used,
- that the original source content was not intentionally rewritten,
- which checks passed,
- any rendering or field-update limitation that remains.
