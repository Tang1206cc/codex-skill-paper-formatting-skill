# word-format-from-content-template

中文 | [English](#english)

## 中文

这是一个用于“按规范和模板排版 Word 文档，同时保持原稿内容不被改写”的 Codex skill。它适合论文、课程报告、毕业设计说明书、公司报告、学校作业、制度文件等需要严格套用格式规范和 Word 模板的场景。

核心目标很明确：用户提供原稿内容、格式规范和 Word 模板后，Codex 使用本 skill 将原稿内容排入模板，并按规范处理字体、段落、页边距、页眉页脚、页码、目录、表格、题注、分页等排版事项。除非用户明确要求改文案，否则不润色、不扩写、不删改、不翻译原稿内容。

对了，其实你可以直接把仓库链接给 codex，让它自己安装。
## Skill 信息

- Skill 名称：`word-format-from-content-template`
- Skill 路径：`skill 包/word-format-from-content-template`
- 入口文件：`skill 包/word-format-from-content-template/SKILL.md`
- 详细工作流：`skill 包/word-format-from-content-template/references/workflow.md`
- 质检清单：`skill 包/word-format-from-content-template/references/quality-checklists.md`
- 文本一致性辅助脚本：`skill 包/word-format-from-content-template/scripts/compare_text.py`

## 适合什么任务

适合使用本 skill 的任务包括：

- 根据学校、学院、课程、公司或期刊的格式要求排版 Word 文件。
- 将论文、报告、作业、毕业设计说明书等原稿套入指定 `.doc` 或 `.docx` 模板。
- 严格保留原稿文字，只调整 Word 排版。
- 清理模板中的示例文字、占位符、旧作者、旧标题、旧正文等残留内容。
- 检查最终文件是否符合格式规范，并尽量渲染成页面图片进行视觉检查。
- 对最终稿和原稿进行文本一致性比对，防止排版过程中误改内容。

不适合使用本 skill 的任务包括：

- 让 Codex 重新写论文、扩写正文、润色语言或补充论点。
- 需要进行学术内容创作、查重降重、参考文献真实性核验的任务。
- 只想做简单文字编辑，而没有明确排版规范或模板的任务。
- 需要排版非 Word 格式成品，例如纯 PDF 设计稿、PPT、网页或 LaTeX 项目。

## 用户调用时应提供哪些材料

为了让 skill 工作稳定，建议用户一次性提供或说明以下材料：

| 材料 | 是否必需 | 说明 |
| --- | --- | --- |
| 原稿内容文件 | 必需 | 需要排版的正文内容，通常是 `.docx`、`.doc`、`.txt`、`.md` 或可提取文字的 PDF。原稿会被视为不可随意改写的内容源。 |
| 格式规范文件 | 必需 | 学校、课程、公司、期刊或导师给出的排版要求，可以是 Word、PDF、图片、网页说明或文字规则。越完整越好。 |
| Word 模板 | 强烈建议 | `.doc` 或 `.docx` 模板，用于继承封面、页眉页脚、样式、章节结构、目录样式等。没有模板时，Codex 可按规范新建文档，但还原度取决于规范细节。 |
| 输出要求 | 建议 | 指定输出文件名、保存目录、是否覆盖旧文件、是否需要同时导出 PDF。默认应生成新文件，不覆盖源文件。 |
| 元信息 | 视情况需要 | 标题、姓名、学号、学院、专业、课程名、指导老师、日期等封面或声明页所需信息。若原稿或模板中缺失，Codex 应询问而不是编造。 |
| 特殊边界 | 建议 | 例如“只排版不改字”“不要改参考文献内容”“目录可以静态生成”“必须能在 Word 中更新目录”等。 |

最理想的输入组合是：

1. 一份明确的原稿文件。
2. 一份完整的格式规范。
3. 一份真实可用的 Word 模板。
4. 一句话说明输出路径和是否允许改动正文。

## 推荐调用方式

用户可以直接在 Codex 中这样说：

```text
Use $word-format-from-content-template to format my draft into the provided Word template according to the formatting specification.

原稿：/path/to/原稿.docx
格式规范：/path/to/格式要求.pdf
Word 模板：/path/to/模板.docx
输出：/path/to/最终排版稿.docx

要求：
1. 只做排版，不改写任何正文内容。
2. 模板里的示例文字不能保留。
3. 完成后请说明做了哪些检查。
```

中文调用示例：

```text
请使用 $word-format-from-content-template 帮我把论文原稿按学校格式规范排进模板里。

原稿文件：/path/to/论文原稿.docx
格式规范：/path/to/论文格式规范.pdf
模板文件：/path/to/学校模板.docx
输出文件：/path/to/论文_排版完成.docx

注意：
- 只允许调整排版，不要润色、删减、扩写或改写正文。
- 封面信息如果原稿和模板里没有，请先问我，不要自己编。
- 最终请检查是否有模板残留，并尽量做渲染视觉检查。
```

更简短的调用也可以：

```text
用 $word-format-from-content-template 处理这个 Word 排版任务。原稿是 A.docx，规范是 B.pdf，模板是 C.docx，输出到 D.docx。只排版，不改内容。
```

## Skill 的工作流程

本 skill 的标准流程如下：

1. 识别输入材料：
   找到格式规范、原稿内容和 Word 模板。如果多个文件容易混淆，先检查文件名和内容；仍不明确时再询问用户。

2. 完整阅读格式规范：
   先把规范读完整，提取纸张、页边距、字体、字号、行距、段落缩进、标题层级、页眉页脚、页码、目录、表格、图题、脚注、参考文献、附录等规则。

3. 锁定原稿内容：
   将原稿文字视为不可随意改写的内容源。允许做样式套用、段落结构识别、目录字段生成等机械排版动作，但不允许改写语句、增删观点、替换术语或更改数字、姓名、日期、引用等关键内容。

4. 检查 Word 模板：
   分析模板中的样式、页眉页脚、节、页码、封面、目录、编号、表格样式和示例内容，决定哪些结构可以继承，哪些需要重建或清理。

5. 生成最终 DOCX：
   将原稿内容写入模板或新文档，按规范显式设置样式、段落、页码、目录、标题编号、题注、表格、分页和节属性。

6. 验证和迭代：
   检查格式规范是否逐项满足，检查最终文本是否与原稿一致，搜索模板残留，并尽量将 DOCX 渲染成 PDF/PNG 页面做视觉检查。

7. 交付说明：
   返回最终 Word 文件路径，说明使用了哪些源文件、完成了哪些检查，以及是否存在目录字段更新或渲染工具限制。

## 内容保护原则

本 skill 最重要的原则是“只排版，不改写内容”。默认禁止：

- 润色句子。
- 总结或压缩段落。
- 扩写论点。
- 翻译内容。
- 删除重复内容。
- 改变术语、姓名、学号、日期、编号、引文、URL、参考文献。
- 自行补充缺失的封面信息、摘要、关键词、致谢或参考文献。

默认允许：

- 套用标题、正文、表格、题注、页眉页脚等样式。
- 按规范设置页边距、字体、字号、行距、缩进、段前段后。
- 根据原稿已有结构分配标题层级。
- 清理模板示例文字和占位文字。
- 生成页码、目录字段、题注字段或静态目录。
- 为满足 Word 排版需要进行有限的空白符规范化。

如果某个排版要求必须补充用户未提供的信息，Codex 应先询问用户，而不是自行编造。

## 质量检查

交付前应尽量完成以下检查：

- 规范一致性：纸张、页边距、字体、字号、行距、段落、标题、页码、页眉页脚、目录、表格、图题、参考文献等是否符合要求。
- 内容一致性：最终文本是否仍保留原稿内容，没有意外改写、删减、扩写或翻译。
- 模板残留：最终文档中是否还有模板旧标题、旧作者、示例正文、占位符、`TODO`、`请更新`、旧页眉页脚等内容。
- 渲染视觉检查：页面是否有文字重叠、裁切、缺字、页码错误、目录错位、表格跨页异常、过大空白等问题。
- 字段限制说明：如果目录或页码字段需要在 Word 中手动更新，应在最终回复中说明。

仓库内的 `scripts/compare_text.py` 可用于辅助比较原稿提取文本和最终稿提取文本：

```bash
python3 "skill 包/word-format-from-content-template/scripts/compare_text.py" source.txt final.txt --loose --show-diff
```

这个脚本会规范化常见空白和 Word 字段噪声，并报告原稿与最终稿文本是否一致。它是辅助工具，不替代人工判断和页面渲染检查。

## 目录结构

```text
codex skill_论文排版工具 skill/
├── README.md
└── skill 包/
    └── word-format-from-content-template/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── workflow.md
        │   └── quality-checklists.md
        └── scripts/
            └── compare_text.py
```

## 安装和使用提示

这个仓库的核心 skill 文件夹是：

```text
skill 包/word-format-from-content-template
```

如果需要安装到 Codex 的 skills 目录，通常应将该文件夹复制到 Codex 的 skills 位置，使 Codex 能识别其中的 `SKILL.md`。安装后，在新会话中可通过 `$word-format-from-content-template` 显式调用，也可以在用户提出“按规范排版 Word、套模板、保持内容不变”等请求时由 Codex 自动触发。

为了提高成功率，用户调用时应尽量使用明确文件路径，不要只说“在附件里”或“帮我排一下”。尤其是多个 Word、PDF、模板同时存在时，明确指出哪个是原稿、哪个是规范、哪个是模板。

## 已知限制

- 目录、交叉引用、页码等 Word 字段在无界面环境下可能无法自动刷新，必要时需要在 Microsoft Word 中打开后更新字段。
- `.doc` 老格式通常需要先转换成 `.docx` 才能稳定处理。
- 扫描版 PDF 或图片规范可能需要 OCR，识别质量会影响规范提取。
- 某些复杂模板的节、页眉页脚、编号和表格边框可能需要 OOXML 级别修复。
- 中文路径或带空格路径可能导致部分渲染工具失败；可临时复制到 ASCII 路径做 QA，但最终交付路径不应因此改变。
- 本 skill 不负责判断论文内容质量、引用真实性、学术规范合规性或查重结果。

## 交付结果应包含

一次合格的最终回复通常应包含：

- 最终 Word 文件路径。
- 使用的原稿、规范和模板文件。
- 是否保持原稿内容不被有意改写。
- 已完成的检查，例如规范清单、文本一致性、模板残留搜索、渲染视觉检查。
- 任何仍需用户在 Word 中处理的事项，例如更新目录字段。

---

## English

This is a Codex skill for formatting Word documents from user-provided content, formatting specifications, and Word templates while preserving the draft text exactly. It is designed for theses, coursework reports, graduation papers, business reports, school assignments, policy documents, and other Word deliverables that must follow strict layout rules.

The core goal is simple: the user provides a draft, a formatting specification, and ideally a Word template; Codex uses this skill to place the draft into the template and apply the required formatting. Unless the user explicitly requests content editing, Codex must not polish, expand, summarize, delete, translate, or rewrite the draft.

By the way, actually you can directly give the repository link to Codex and let it install by itself.
## Skill Information

- Skill name: `word-format-from-content-template`
- Skill path: `skill 包/word-format-from-content-template`
- Entry file: `skill 包/word-format-from-content-template/SKILL.md`
- Detailed workflow: `skill 包/word-format-from-content-template/references/workflow.md`
- QA checklist: `skill 包/word-format-from-content-template/references/quality-checklists.md`
- Text comparison helper: `skill 包/word-format-from-content-template/scripts/compare_text.py`

## What This Skill Is For

Use this skill for tasks such as:

- Formatting a Word document according to school, course, company, journal, or institutional rules.
- Applying a `.doc` or `.docx` template to a thesis, report, assignment, or formal document.
- Preserving the original draft text while changing only layout and Word formatting.
- Removing sample text, placeholders, old titles, old authors, and old body content from a template.
- Checking whether the final file follows the specification.
- Comparing final extracted text against the source draft to catch accidental content changes.

This skill is not intended for:

- Rewriting, polishing, expanding, or improving the paper content.
- Academic writing, plagiarism reduction, or validating the truth of references.
- Simple text editing without a formatting specification or template.
- Producing non-Word deliverables such as designed PDFs, PowerPoint decks, websites, or LaTeX projects.

## What Users Should Provide

For best results, users should provide or clearly identify these materials:

| Material | Required | Notes |
| --- | --- | --- |
| Source draft | Required | The content to format, usually `.docx`, `.doc`, `.txt`, `.md`, or a text-extractable PDF. The draft is treated as immutable content. |
| Formatting specification | Required | Formatting rules from a school, course, company, journal, supervisor, or institution. It may be a Word file, PDF, image, webpage, or plain text. |
| Word template | Strongly recommended | A `.doc` or `.docx` template that carries the cover, styles, headers, footers, section structure, TOC style, and page setup. |
| Output requirements | Recommended | Output file name, destination folder, overwrite policy, and whether a PDF export is also needed. The default should be to create a new file and preserve source files. |
| Metadata | Sometimes required | Title, author name, student ID, department, major, course, supervisor, date, and other cover/front-matter fields. Missing required information should be requested, not invented. |
| Special boundaries | Recommended | For example: "format only, do not edit text", "do not change references", "static TOC is acceptable", or "TOC must be updateable in Word". |

The ideal input set is:

1. A clear source draft file.
2. A complete formatting specification.
3. A real Word template.
4. A short instruction for the output path and whether content edits are allowed.

## Recommended Prompts

Example:

```text
Use $word-format-from-content-template to format my draft into the provided Word template according to the formatting specification.

Draft: /path/to/draft.docx
Specification: /path/to/formatting-rules.pdf
Template: /path/to/template.docx
Output: /path/to/final-formatted.docx

Requirements:
1. Format only. Do not rewrite any body text.
2. Remove all sample text from the template.
3. Tell me which checks were completed.
```

Chinese example:

```text
请使用 $word-format-from-content-template 帮我把论文原稿按学校格式规范排进模板里。

原稿文件：/path/to/论文原稿.docx
格式规范：/path/to/论文格式规范.pdf
模板文件：/path/to/学校模板.docx
输出文件：/path/to/论文_排版完成.docx

注意：
- 只允许调整排版，不要润色、删减、扩写或改写正文。
- 封面信息如果原稿和模板里没有，请先问我，不要自己编。
- 最终请检查是否有模板残留，并尽量做渲染视觉检查。
```

Short prompt:

```text
Use $word-format-from-content-template for this Word formatting task. Draft is A.docx, spec is B.pdf, template is C.docx, output to D.docx. Format only; do not edit content.
```

## Workflow

The skill follows this workflow:

1. Identify inputs:
   Locate the formatting specification, source draft, and Word template. If files are ambiguous after inspection, ask the user a concise question.

2. Read the full specification:
   Extract all relevant rules for page setup, margins, fonts, line spacing, paragraph indents, heading hierarchy, page breaks, headers, footers, page numbering, TOC, tables, figures, captions, footnotes, references, and appendices.

3. Lock the draft content:
   Treat the source draft as immutable. Codex may assign styles, generate fields, and make mechanical layout adjustments, but must not rewrite sentences, change terminology, delete content, alter numbers, or invent missing metadata.

4. Inspect the template:
   Analyze styles, sections, headers, footers, cover blocks, TOC fields, numbering, table styles, and sample text. Decide what can be reused and what must be rebuilt or removed.

5. Produce the final DOCX:
   Insert the draft content into the template or a new document, then explicitly apply the required styles, paragraph settings, page numbering, TOC behavior, heading numbering, captions, tables, page breaks, and section properties.

6. Verify and iterate:
   Check specification compliance, compare final text against the source draft, search for template residue, and render the DOCX to PDF/PNG pages when tooling permits.

7. Report delivery:
   Return the final Word path, source files used, checks performed, and any remaining limitations such as Word field update requirements.

## Content Preservation Rules

The most important rule is: format the document, do not rewrite the content.

By default, Codex must not:

- Polish sentences.
- Summarize or compress paragraphs.
- Expand arguments.
- Translate content.
- Remove repetitive content.
- Change terms, names, student IDs, dates, numbers, citations, URLs, or references.
- Invent missing title-page, abstract, keyword, acknowledgement, or bibliography content.

By default, Codex may:

- Apply styles for headings, body text, tables, captions, headers, and footers.
- Set margins, fonts, font sizes, line spacing, indents, paragraph spacing, and alignment.
- Assign heading levels based on the draft's existing structure.
- Remove template sample text and placeholders.
- Generate page numbers, TOC fields, caption fields, or a static TOC.
- Normalize limited whitespace when Word layout requires it.

If a required formatting element needs information the user has not provided, Codex should ask the user instead of inventing it.

## Quality Checks

Before delivery, Codex should complete as many of these checks as possible:

- Specification compliance: page setup, margins, fonts, font sizes, line spacing, paragraphs, headings, page numbers, headers/footers, TOC, tables, figure captions, and references.
- Content identity: final text still matches the draft and contains no accidental rewriting, deletion, expansion, or translation.
- Template residue: no old title, old author, sample body text, placeholder, `TODO`, stale header/footer, or unrelated template content remains.
- Rendered visual QA: no overlapping text, clipping, missing glyphs, wrong page numbers, broken TOC alignment, awkward table breaks, or excessive blank space.
- Field limitations: any TOC, cross-reference, or page-number field that must be updated manually in Word should be disclosed.

The bundled helper can compare extracted draft text and extracted final text:

```bash
python3 "skill 包/word-format-from-content-template/scripts/compare_text.py" source.txt final.txt --loose --show-diff
```

The script normalizes common whitespace and Word field noise, then reports whether the normalized texts match. It is a helper, not a replacement for human review and rendered page inspection.

## Repository Structure

```text
codex skill_论文排版工具 skill/
├── README.md
└── skill 包/
    └── word-format-from-content-template/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── workflow.md
        │   └── quality-checklists.md
        └── scripts/
            └── compare_text.py
```

## Installation and Usage Notes

The actual skill folder is:

```text
skill 包/word-format-from-content-template
```

To install it into Codex, copy that folder into the Codex skills directory so Codex can discover its `SKILL.md`. After installation, users can call it explicitly with `$word-format-from-content-template`, or Codex may invoke it automatically when the request asks to format a Word document from a template while preserving content.

For reliable results, users should provide explicit file paths and identify which file is the draft, which file is the specification, and which file is the template. This is especially important when a folder contains multiple Word and PDF files.

## Known Limitations

- TOC, cross-reference, and page-number fields may not refresh correctly in headless environments; Microsoft Word may be needed to update fields.
- Legacy `.doc` files often need conversion to `.docx` before stable processing.
- Scanned PDFs or image-only specifications may require OCR, and OCR quality affects rule extraction.
- Complex templates may require direct OOXML edits for sections, headers/footers, numbering, or table borders.
- Chinese paths or paths with spaces may break some rendering tools; temporary ASCII paths can be used for QA while preserving the final output path.
- This skill does not evaluate academic content quality, reference truthfulness, plagiarism status, or scholarly compliance.

## Expected Delivery

A good final response from Codex should include:

- Final Word file path.
- Draft, specification, and template files used.
- A statement that source content was not intentionally rewritten.
- Checks completed, such as specification checklist, text identity comparison, template-residue search, and rendered visual QA.
- Any remaining action for the user, such as updating fields in Microsoft Word.
