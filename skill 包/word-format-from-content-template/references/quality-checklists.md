# Quality Checklists

Use these checklists before delivering a formatted Word document.

## A. Specification Compliance

- [ ] Full specification file was read, not skimmed.
- [ ] Output page size, orientation, margins, gutter, header/footer distance match the spec.
- [ ] Base Chinese font, Latin font, font sizes, line spacing, paragraph spacing, and first-line indents match the spec.
- [ ] Heading levels, numbering, alignment, font, spacing, and page-break behavior match the spec.
- [ ] Required front matter exists in the required order.
- [ ] TOC includes the required heading levels and correct page numbers, or a field-update limitation is explicitly disclosed.
- [ ] Page numbering format and restart rules are correct across front matter and body sections.
- [ ] Headers and footers appear only where required and use the required text, alignment, rule lines, and font.
- [ ] Tables use required caption placement, numbering, font, line style, width, and page behavior.
- [ ] Figures, equations, notes, references, appendices, and acknowledgements follow the spec when present.
- [ ] Built-in Word styles do not leak unwanted theme color, font, spacing, or numbering.

## B. Content Identity

- [ ] Draft content was extracted before formatting and treated as immutable.
- [ ] Final text contains the same user-provided content, except for allowed mechanical layout changes.
- [ ] Names, student IDs, dates, numbers, citations, URLs, and technical terms are unchanged unless explicitly requested.
- [ ] No sentences were rewritten, polished, summarized, translated, deleted, or expanded.
- [ ] Any required missing front-matter content was requested from the user instead of invented.
- [ ] `scripts/compare_text.py` or an equivalent comparison was run when feasible.
- [ ] All detected differences were reviewed and classified as expected formatting artifacts or fixed.

## C. Template Residue

- [ ] Old sample title, topic, author, organization, project name, course name, and placeholder strings were removed.
- [ ] No `TODO`, `请更新`, `placeholder`, sample bibliography, or unrelated old content remains.
- [ ] Template headers/footers do not contain stale text.
- [ ] Template fields do not display stale or placeholder values after render.
- [ ] Final file metadata is updated when relevant and does not mislead the user.

## D. Render and Visual QA

- [ ] Final DOCX was rendered to PDF/PNG, or a rendering limitation was documented.
- [ ] Cover and front matter are visually clean.
- [ ] Page numbers are visible, centered/aligned as required, and in the correct numeral style.
- [ ] Each required new page or chapter break occurs correctly.
- [ ] No text overlaps, clipping, missing glyphs, excessive blank gaps, or boundary-hugging table text.
- [ ] Tables are not broken awkwardly across headers/footers; long tables are handled intentionally.
- [ ] TOC lines, dot leaders, and page numbers align.
- [ ] Last pages, references, appendices, and acknowledgements are complete.

## E. Delivery

- [ ] Source files were not overwritten unless explicitly requested.
- [ ] Final output path is clear and meaningful.
- [ ] QA intermediates are not presented as deliverables unless requested.
- [ ] Final response states the final DOCX path and the verification performed.
