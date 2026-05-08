# Workflow: Format Word From Content, Specification, and Template

Use this workflow when the user provides a formatting specification, an immutable draft, and a Word template. The output should be the user's content, formatted into the template according to every applicable rule.

## 1. Input Discovery

Confirm the three source categories by inspection:

- **Formatting specification**: school/company format rules, thesis/report standard, rubric, style guide, or sample requirement file.
- **Immutable draft**: the exact user-provided content to place into the final document.
- **Word template**: `.doc` or `.docx` file whose structure, cover, styles, or page furniture should carry the final content.

If a file is missing or ambiguous after inspection, ask a concise question. Otherwise proceed.

Preserve source files. Generate a new output path unless the user explicitly requests overwriting.

## 2. Read the Full Specification First

Do not begin production from memory or from the template alone. Extract and read the entire specification before implementing.

Recommended extraction approach:

- `.doc/.docx`: use `textutil -convert txt -stdout`, then inspect the DOCX/OOXML if style details matter.
- `.pdf`: use PDF extraction and visual rendering for layout examples.
- image scans: use OCR if available, then visually inspect important pages.
- mixed specifications: combine extracted text with screenshots/PNG render review.

Build a formatting contract from the specification. At minimum capture:

- paper size, orientation, margins, gutter, header/footer distance,
- base fonts, Chinese/Latin font split, font size, line spacing, paragraph spacing,
- first-line indent, alignment, character spacing, grid settings if specified,
- title page, cover metadata, declaration pages, abstract, keywords, TOC,
- heading numbering, heading levels, page-break rules,
- page headers, footers, page numbering format and restart points,
- tables, figures, captions, notes, references, appendices, acknowledgements,
- special rules such as "each chapter starts on a new page" or "TOC includes level 3".

## 3. Lock the Draft Content

Extract the user's source draft as a separate text artifact for comparison. Treat it as immutable.

Allowed mechanical transformations:

- apply paragraph and heading styles,
- split or merge paragraphs only when the source already implies that structure,
- remove template placeholders,
- generate page numbers, TOC fields, captions, and cross-reference fields,
- normalize invisible whitespace when Word requires it.

Not allowed unless the user asks:

- rewrite sentences,
- add new arguments or examples,
- delete repetitive content,
- change terminology,
- translate content,
- alter names, dates, IDs, citations, or numbers.

If the draft is under-specified for required front matter, ask before inventing content.

## 4. Inspect the Template

Open/extract the template before writing:

- identify reusable styles, section breaks, headers, footers, page setup, cover blocks, TOC fields, numbering, and table styles,
- identify sample text and placeholder content that must be removed,
- decide whether to preserve the template structure directly or rebuild it with explicit styles.

If using the template as a base, ensure final content does not retain unrelated old sample content. Run targeted searches for template topic words, old names, placeholder labels, and TODO strings.

## 5. Implement the DOCX

Use the least fragile route that still satisfies the specification:

- High-level `.docx` creation/editing: `python-docx`.
- Precise fields/section/page-numbering/table geometry: OOXML edits.
- Legacy `.doc`: convert to `.docx` for production when possible, while preserving original files.
- Complex visual QA: render the DOCX to PDF/PNG and inspect.

Apply specification values explicitly. Avoid relying on Word defaults for margins, font, headings, lists, table widths, header/footer text, or page numbering when the spec defines them.

When TOC fields do not update reliably in headless renderers, choose one of these safe options:

- create a real TOC field and state it must be updated in Word, if the user accepts that workflow,
- or create a static TOC with verified page numbers when the deliverable must render correctly without field update.

## 6. Format-Specific Pitfalls From Practice

- **TOC fields**: headless conversion may show placeholder text or stale page numbers. Verify rendered output, not just XML.
- **Tables**: long tables may split awkwardly across pages. Render and inspect; move a table to a new page or allow proper repeated headers if needed.
- **Headers/footers**: section breaks can silently inherit previous headers or numbering. Explicitly unlink sections when restarting page numbering.
- **Font color/style leakage**: built-in Word heading styles may carry blue or theme styling. Patch styles to match the spec exactly.
- **Template residue**: final text extraction should not contain old topics, old names, sample company/school text, or placeholder instructions.
- **Chinese paths in render tools**: if rendering fails, copy the DOCX to a temporary ASCII path for QA only.

## 7. Verify and Iterate

Use a two-axis verification loop:

1. **Specification compliance**: check every item in the formatting contract.
2. **Content identity**: compare extracted final text against the immutable draft and inspect any differences.

Recommended checks:

- extract final DOCX text and search for template residue,
- run `scripts/compare_text.py` on extracted source/final body text when feasible,
- render final pages to PNG,
- inspect cover, front matter, first body page, every table page, section transitions, last body page, and references/appendices,
- repeat after every meaningful formatting fix.

## 8. Final Response

Report only what matters:

- final file path,
- source files used,
- checks performed,
- any known limitation, especially if visual rendering or field update could not be completed.
