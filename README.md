# MATEL — Malware Intelligence

**MATEL: Malware Intelligence and Threat Intelligence Analysis of Malware Campaigns**
UTS Malware Analysis — Proyek 25: Threat Intelligence Report (Malware Campaign)

Analisis intelijen ancaman **pasif / berbasis IOC** untuk tiga pelaku:

| Pelaku | Malware utama | MITRE ATT&CK |
|---|---|---|
| TA542 | Emotet | S0367 |
| TA505 | Dridex | S0384 / G0092 |
| FIN6 | FrameworkPOS, More_eggs, HARDBREAD, Ryuk | G0037 |

## Batasan keselamatan

Seluruh pekerjaan bersifat **pasif**. Tidak ada sampel yang dijalankan, tidak ada muatan
yang diunduh, tidak ada pemindaian atau eksploitasi infrastruktur, dan tidak ada koneksi
ke command and control. Permintaan jaringan hanya menuju titik akhir metadata publik
(Crossref, Unpaywall) dan berkas indikator resmi yang diterbitkan lembaga.

## Hasil utama

| Artefak | Lokasi | Isi |
|---|---|---|
| Laporan final | `MATEL_Threat_Intelligence_Report.docx` / `.pdf` | 25 halaman, 6 gambar, 12 tabel |
| Indikator | `ioc/*.csv` | 36 baris ternormalisasi (TA542 7, TA505 29, FIN6 0) |
| Pemetaan teknik | `ttp_mapping.json` | 70 baris teknik terdokumentasi, tiap baris membawa kalimat bukti |
| Pustaka | `references.ris`, `references.bib`, `refs_final.json` | 34 artikel, DOI + akses terbuka terverifikasi |
| Validasi pustaka | `reference_validation.md` | tabel verifikasi per artikel |
| Bukti | `evidence/` | advisory CISA (CSV + STIX), cuplikan Feodo, basis ATT&CK, korpus akademik |
| Diagram | `figures/*.html`, `figures/*.png` | 8 diagram Archify dengan bukti pemeriksaan otomatis |

## Reproduksi

```bash
python3 build_iocs.py            # kumpulkan + normalisasi indikator dari sumber resmi
python3 validate_references.py   # selesaikan DOI via Crossref, cek OA via Unpaywall
python3 make_refs.py             # tulis references.ris / .bib / tabel validasi
python3 build_report.py          # isi template dosen, hasilkan DOCX
soffice --headless --convert-to pdf MATEL_Threat_Intelligence_Report.docx
```

Diagram dibangun dengan [Archify](https://github.com/tt-a1i/archify); setiap preset ada di
`archify/` dan setiap keluaran disertai berkas `*.finalize.json` sebagai bukti gate.

## Status yang tidak diklaim

Status indeks **Scopus** dan peringkat **SINTA** tidak dapat diverifikasi secara independen
pada lingkungan ini. Semua baris validasi menuliskan `Not independently verified`; laporan
tidak mengklaim kuartil maupun peringkat apa pun.

Untuk FIN6 tidak ditemukan indikator jaringan pada sumber yang dianalisis. `ioc/fin6_ioc.csv`
sengaja dibiarkan kosong dan fakta itu dinyatakan di dalam laporan, bukan diisi dengan nilai
rekaan.
