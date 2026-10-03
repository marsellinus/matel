#!/usr/bin/env python3
"""MATEL report builder - fills the lecturer template in place.

Every original run, style, section, margin, font and table object is preserved.
Text is substituted only through existing paragraph runs; new content is appended
using the template's own style objects.
"""
import os

from docx import Document
from docx.shared import Pt

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(ROOT, "Template_Laporan_Kegiatan_Malware_Analysis_2026.docx")
OUTPUT = os.path.join(ROOT, "MATEL_Threat_Intelligence_Report.docx")

import content_report as C


def set_paragraph_text(p, text):
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.add_run(text)


def replace_placeholder(doc, needle, text):
    for p in doc.paragraphs:
        if needle in p.text:
            set_paragraph_text(p, text)
            return True
    return False


def cell_replace(doc, needle, text):
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                if needle in c.text:
                    for p in c.paragraphs:
                        if needle in p.text:
                            set_paragraph_text(p, p.text.replace(needle, text))
                    return True
    return False


def fill_table(doc, index, rows):
    t = doc.tables[index]
    body = t.rows[1:]
    for i, values in enumerate(rows):
        row = body[i] if i < len(body) else t.add_row()
        for j, v in enumerate(values):
            cell = row.cells[j]
            cell.text = ""
            cell.paragraphs[0].add_run(str(v))


def add_heading(doc, text, level):
    p = doc.add_paragraph(style="Heading %d" % level)
    p.add_run(text)


def add_body(doc, text):
    p = doc.add_paragraph(style="Normal")
    p.add_run(text)


def add_caption(doc, text):
    p = doc.add_paragraph(style="Normal")
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(9)


def add_bullets(doc, items):
    for it in items:
        p = doc.add_paragraph(style="List Paragraph")
        p.add_run(it)


def add_table(doc, headers, rows):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = ""
        r = c.paragraphs[0].add_run(h)
        r.bold = True
    for values in rows:
        cells = t.add_row().cells
        for i, v in enumerate(values):
            cells[i].text = ""
            cells[i].paragraphs[0].add_run(str(v))


def build():
    doc = Document(TEMPLATE)

    for k, v in C.IDENT.items():
        cell_replace(doc, k, v)

    cell_replace(doc, "Nama/jenis sampel", "Nama/jenis objek analisis")
    cell_replace(doc, "Hash / pengenal", "Pengenal kampanye")
    cell_replace(doc, "Ukuran dan format/arsitektur", "Bentuk artefak")
    cell_replace(doc, "Sumber artefak", "Sumber bukti")
    cell_replace(doc, "Waktu pengamatan", "Waktu pengamatan")
    for row in doc.tables[1].rows[1:]:
        label = row.cells[0].text.strip()
        if label in C.SAMPLE:
            row.cells[1].text = ""
            row.cells[1].paragraphs[0].add_run(C.SAMPLE[label])

    replace_placeholder(doc, "[Tulis ringkasan maksimal dua halaman", C.EXEC_SUMMARY)
    replace_placeholder(doc, "Uraian kasus, alasan analisis", C.SECTION_1_1)
    replace_placeholder(doc, "Objek analisis, artefak yang tersedia", C.SECTION_1_2)
    replace_placeholder(doc, "Petunjuk pengisian:", C.INSTRUCTION_NOTE)
    replace_placeholder(doc, "Catat setiap langkah yang benar-benar dilakukan", C.INSTRUCTION_NOTE_2)
    replace_placeholder(doc, "[Uraikan urutan kerja secara ringkas", C.SECTION_3)
    replace_placeholder(doc, "[Susun urutan kejadian yang didukung timestamp", C.SECTION_4_2)
    replace_placeholder(doc, "UTS: triage dan minimal tiga hipotesis", C.SECTION_5_INTRO)
    replace_placeholder(doc, "UAS: anti-reverse engineering", C.SECTION_5_INTRO_UAS)
    replace_placeholder(doc, "Proyek pilihan: cantumkan nomor", C.SECTION_5)
    replace_placeholder(doc, "Verdict analis:", C.SECTION_6_VERDICT)
    replace_placeholder(doc, "Kesimpulan:", C.SECTION_7)
    replace_placeholder(doc, "Daftar pustaka:", "")
    replace_placeholder(doc, "Lampiran:", C.SECTION_APPENDIX)

    fill_table(doc, 2, C.HYPOTHESES)
    fill_table(doc, 3, C.ACTIVITY)

    for idx, rows in ((4, C.EVIDENCE), (5, C.FINDINGS), (6, C.IOC_SUMMARY)):
        t = doc.tables[idx]
        while len(t.rows) - 1 < len(rows):
            t.add_row()
        while len(t.rows) - 1 > len(rows):
            t._tbl.remove(t.rows[-1]._tr)
        fill_table(doc, idx, rows)

    fill_table(doc, 7, C.RECOMMENDATIONS)

    doc.add_page_break()
    for heading, level, blocks in C.PROJECT_SECTIONS:
        add_heading(doc, heading, level)
        for kind, payload in blocks:
            if kind == "p":
                add_body(doc, payload)
            elif kind == "bullets":
                add_bullets(doc, payload)
            elif kind == "caption":
                add_caption(doc, payload)
            elif kind == "table":
                headers, rows, caption = payload
                add_table(doc, headers, rows)
                add_caption(doc, caption)
            elif kind == "figure":
                path, caption = payload
                full = os.path.join(ROOT, path)
                if os.path.exists(full):
                    doc.add_picture(full, width=Pt(430))
                add_caption(doc, caption)

    add_heading(doc, "Daftar Pustaka", 1)
    add_body(doc, C.REF_INTRO)
    for i, e in enumerate(C.REFERENCES, 1):
        add_body(doc, "[%d] %s" % (i, e))
    add_heading(doc, "Sumber Intelijen Teknis (bukan artikel akademik)", 2)
    for e in C.TECHNICAL_SOURCES:
        add_body(doc, e)

    doc.save(OUTPUT)
    print("saved", OUTPUT)


if __name__ == "__main__":
    build()
