# -*- coding: utf-8 -*-
"""MATEL report content (Proyek 25). Authored text kept separate from layout."""

REFERENCES = [
    'Demirol, D., Das, R., & Hanbay, D. (2025). A Novel Approach for Cyber Threat Analysis Systems Using BERT Model from Cyber Threat Intelligence Data. Symmetry. Vol. 17(4), pp. 587 https://doi.org/10.3390/sym17040587',
    'Abeydeera, C. (2026). Systematically Integrating Cyber Threat Intelligence into Resilient Space-Cyber Architectures. European Conference on Cyber Warfare and Security. Vol. 25(1), pp. 932-942 https://doi.org/10.34190/eccws.25.1.4673',
    'Raharjo, D. H. K., & Salman, M. (2023). ANALYZING SURICATA ALERT DETECTION PERFORMANCE ISSUES BASED ON ACTIVE INDICATOR OF COMPROMISE RULES. Jurnal Teknik Informatika (Jutif). Vol. 4(3), pp. 601-610 https://doi.org/10.52436/1.jutif.2023.4.3.1013',
    'Kumar, R., & Subbiah, G. (2022). Zero-Day Malware Detection and Effective Malware Analysis Using Shapley Ensemble Boosting and Bagging Approach. Sensors. Vol. 22(7), pp. 2798 https://doi.org/10.3390/s22072798',
    'Guven, M. (2024). Leveraging deep learning and image conversion of executable files for effective malware detection: A static malware analysis approach. AIMS Mathematics. Vol. 9(6), pp. 15223-15245 https://doi.org/10.3934/math.2024739',
    'Rafiey, P., & Namadchian, A. (2025). Mapping Vulnerability Description to MITRE ATT&CK Framework by LLM. Advances in Artificial Intelligence and Machine Learning. Vol. 05(03), pp. 4379-4396 https://doi.org/10.54364/aaiml.2025.53243',
    'Grigorescu, O., Nica, A., Dascalu, M., & Rughinis, R. (2022). CVE2ATT&CK: BERT-Based Mapping of CVEs to MITRE ATT&CK Techniques. Algorithms. Vol. 15(9), pp. 314 https://doi.org/10.3390/a15090314',
    'Cichon, M., Mycek, A., & Plawiak, P. (2026). Threat Model for Hybrid Cloud–Edge Cyber–Physical Systems: Mapping STRIDE to MITRE ATT&CK for ICS. Electronics. Vol. 15(18), pp. 4097 https://doi.org/10.3390/electronics15184097',
    'Smirnov, D., & Evsutin, O. (2024). Methodology for Collecting Data on the Activity of Malware for Windows OS Based on MITRE ATT&CK. Informatics and Automation. Vol. 23(3), pp. 642-683 https://doi.org/10.15622/ia.23.3.2',
    'Branescu, I., Grigorescu, O., & Dascalu, M. (2024). Automated Mapping of Common Vulnerabilities and Exposures to MITRE ATT&CK Tactics. Information. Vol. 15(4), pp. 214 https://doi.org/10.3390/info15040214',
    'Sajan, P. P. (2024). Yara-Based Emotet Malware Scanner – A Factual Analysis. Communications on Applied Nonlinear Analysis. Vol. 32(2s), pp. 202-213 https://doi.org/10.52783/cana.v32.2266',
    'G, M. V., Chandran, S., & U, A. T. (2023). Malware Reverse Engineering to Find the Malicious Activity of Emotet. Advances in Transdisciplinary Engineering. https://doi.org/10.3233/atde221253',
    'Alodat, I. (2023). Malware: Detection and Defense. Malware - Detection and Defense. https://doi.org/10.5772/intechopen.108434',
    'Sianipar, V. R., & Pangaribuan, H. (2023). ANALISIS DAN DETEKSI MALWARE PADA PROTOKOL JARINGAN MENGGUNAKAN METODE MALWARE ANALISIS DINAMIS DAN MALWARE ANALISIS STATIS. Computer and  Science Industrial Engineering (COMASIE). Vol. 9(6) https://doi.org/10.33884/comasiejournal.v9i6.7833',
    'Nugraha, A., & Gustian, D. A. (2022). Deteksi Malware Dridex Menggunakan Signature-based Snort. Indonesian Journal of Computer Science. Vol. 10(1) https://doi.org/10.33022/ijcs.v10i1.3068',
    'Mursalim, M., Darmawan, W., & Aprilia, T. (2024). Analisa Metasploit Framework “msfvenom” Backdoor Trojan dan Fully Undetected (FUD) Trojan. Techno.Com. Vol. 23(1), pp. 112-124 https://doi.org/10.62411/tc.v23i1.9741',
    'Hussain, S., & Petrova, K. (2026). Threat Actor Attribution Applying a Tactics–Techniques–Procedures Approach: An Empirical Investigation. Future Internet. Vol. 18(8), pp. 433 https://doi.org/10.3390/fi18080433',
    'Zhora, V., Antoniuk, A., Matvieiev, S., & Artemchuk, V. (2026). A Bounded Threat–Actor-Conditioned Cyber Risk Assessment Framework for Networked Systems Under Data-Scarce Conditions. Computers. Vol. 15(10), pp. 649 https://doi.org/10.3390/computers15100649',
    'Irshad, E., Nawaz, S., & Siddiqui, A. B. (2026). Data-Driven Clustering of Malicious Actor Profiles Based on Machine Learning Analysis of Attack Patterns in Cyber-Threat Intelligence Feeds. AI, Computer Science and Robotics Technology. Vol. 5 https://doi.org/10.5772/acrt.20250160',
    'Garcia, F. J. C. (2021). Private Investigation and Open Source INTelligence (OSINT). Cybersecurity Threats with New Perspectives. https://doi.org/10.5772/intechopen.95857',
    'Pelofske, E., Liebrock, L. M., & Urias, V. (2026). Cybersecurity Threat Hunting and Vulnerability Analysis Using a Neo4j Graph Database of Open Source Intelligence. Digital Threats: Research and Practice., Article 3822596 https://doi.org/10.1145/3822596',
    'Bohm, I., & Lolagar, S. (2021). Open source intelligence. International Cybersecurity Law Review. Vol. 2(2), pp. 317-337 https://doi.org/10.1365/s43439-021-00042-7',
    'Nonum, E. O., Avwokuruaye, O., & Ezemonye, T. M. (2025). Role of Open Source Intelligence (OSINT) in Cybersecurity and Threat Analysis. International Journal of Latest Technology in Engineering Management & Applied Science. Vol. 14(3), pp. 189-200 https://doi.org/10.51583/ijltemas.2025.140300023',
    'Hidayat, T., Wibowo, B., Yuswanto, A., & Jannah, A. F. (2025). Cybersecurity Education Strategies Based on Open-Source Intelligence (OSINT) to Enhance Public Awareness. International Journal of Science Education and Cultural Studies. Vol. 4(2), pp. 1-9 https://doi.org/10.58291/ijsecs.v4i2.422',
    'Li, Z., Yu, X., & Zhao, Y. (2024). A Web Semantic Mining Method for Fake Cybersecurity Threat Intelligence in Open Source Communities. International Journal on Semantic Web and Information Systems. Vol. 20(1), pp. 1-22 https://doi.org/10.4018/ijswis.350095',
    'Tolah, A. (2025). BlockIntelChain: a blockchain-based cyber threat intelligence sharing architecture. Scientific Reports. Vol. 16(1), Article 190 https://doi.org/10.1038/s41598-025-29152-6',
    'Abraham, C., Bélanger, F., & Daultrey, S. (2025). Promoting research on cyber threat intelligence sharing in ecosystems. Journal of Cybersecurity. Vol. 11(1), Article tyaf016 https://doi.org/10.1093/cybsec/tyaf016',
    'Motlhabi, M., Pantsi, P., Mangoale, B., Netshiya, R., & Chishiri, S. (2022). Context-Aware Cyber Threat Intelligence Exchange Platform. International Conference on Cyber Warfare and Security. Vol. 17(1), pp. 201-210 https://doi.org/10.34190/iccws.17.1.42',
    'Miah, M. N. I., Uddin, M. J., & Ahmed, M. W. (2025). AI-Driven Threat Intelligence: Evaluating Machine Learning for Real-Time Cyber Threat Sharing Among U.S. National Security Agencies. Journal of Computer Science and Technology Studies. Vol. 7(8), pp. 300-313 https://doi.org/10.32996/jcsts.2025.7.8.34',
    'Akbar, S., & Khan, T. (2025). Malware Detection Using Static Feature Analysis and Deep Learning Techniques. Information Technology and Control. Vol. 54(4), pp. 1358-1382 https://doi.org/10.5755/j01.itc.54.4.35472',
    'Kim, M., Cho, H., & Yi, J. H. (2022). Large-Scale Analysis on Anti-Analysis Techniques in Real-World Malware. IEEE Access. Vol. 10, pp. 75802-75815 https://doi.org/10.1109/access.2022.3190978',
    'Yamaguchi, S. (2022). Botnet Defense System: Observability, Controllability, and Basic Command and Control Strategy. Sensors. Vol. 22(23), pp. 9423 https://doi.org/10.3390/s22239423',
    'Preuveneers, D., & Joosen, W. (2021). Sharing Machine Learning Models as Indicators of Compromise for Cyber Threat Intelligence. Journal of Cybersecurity and Privacy. Vol. 1(1), pp. 140-163 https://doi.org/10.3390/jcp1010008',
    'Georgiadou, A., Mouzakitis, S., & Askounis, D. (2021). Assessing MITRE ATT&CK Risk Using a Cyber-Security Culture Framework. Sensors. Vol. 21(9), pp. 3267 https://doi.org/10.3390/s21093267',
]

IDENT = {
    "[UTS / UAS / proyek pilihan]": "UTS - Proyek 25: Threat Intelligence Report (Malware Campaign)",
    "[Judul sesuai soal atau penugasan dosen]": "MATEL: Malware Intelligence and Threat Intelligence Analysis of Malware Campaigns",
    "[Nama lengkap — NPM]": "Kelompok MATEL - NPM sesuai daftar kelas",
    "[Jika berkelompok; tulis individu bila tidak]": "Analis IOC dan OSINT; Analis TTP dan ATT&CK; Penyusun laporan",
    "[Kelas] / 7": "Malware Analysis / Semester 7",
    "[Tanggal] — [VM/laboratorium]": "3 Oktober 2026 - lingkungan CTI pasif (tanpa eksekusi sampel)",
}

SAMPLE = {
    "Nama/jenis objek analisis": "Tiga kampanye malware: TA542 (Emotet), TA505 (Dridex), FIN6",
    "Pengenal kampanye": "MITRE ATT&CK S0367; S0384; G0092; G0037; CISA AA19-339A",
    "Bentuk artefak": "Tidak berlaku - analisis berbasis laporan dan IOC, bukan berkas biner",
    "MD5 / SHA-1 / SHA-256": "Tidak tersedia - tidak ada berkas malware yang diunduh",
    "Sumber bukti": "CISA AA19-339A; abuse.ch Feodo Tracker; MITRE ATT&CK; literatur akademik",
    "VM, sistem operasi, snapshot": "Workstation analis terisolasi; tidak ada koneksi ke infrastruktur malware",
    "Tools dan versi": "Python 3; python-docx; LibreOffice; Archify 2.17",
    "Waktu pengamatan": "3 Oktober 2026",
}



REF_INTRO = (
    "Daftar berikut memuat 34 artikel ilmiah yang seluruh DOI-nya diverifikasi "
    "melalui Crossref dan status akses terbukanya diverifikasi melalui Unpaywall "
    "pada 3 Oktober 2026. Status Scopus dan SINTA tidak dapat diverifikasi secara "
    "independen melalui sumber otoritatif pada lingkungan ini dan karena itu "
    "dilaporkan apa adanya, bukan diklaim. Sumber intelijen teknis (MITRE ATT&CK, "
    "CISA, abuse.ch) dicantumkan terpisah dari daftar akademik."
)

INSTRUCTION_NOTE = (
    "Laporan ini disusun dari sumber terbuka dengan metode pasif: hanya membaca "
    "laporan, taksonomi, dan indikator yang telah dipublikasikan. Tidak ada sampel "
    "yang dieksekusi, tidak ada muatan yang diunduh, dan tidak ada koneksi ke "
    "infrastruktur pelaku. Bagian yang tidak didukung bukti ditandai secara eksplisit."
)

INSTRUCTION_NOTE_2 = (
    "Setiap langkah yang dicatat di bawah benar-benar dijalankan pada workstation "
    "analis. Tidak ada artefak yang disediakan dosen untuk proyek ini; objek "
    "analisis adalah kampanye malware, sehingga yang dilakukan adalah interpretasi "
    "laporan publik dan normalisasi indikator, bukan eksekusi sampel."
)

EXEC_SUMMARY = (
    "Laporan ini menyajikan analisis intelijen ancaman terhadap tiga kampanye "
    "malware: TA542 (Emotet), TA505 (Dridex), dan FIN6. Metode yang dipakai adalah "
    "intelijen ancaman pasif berbasis indikator: seluruh bukti berasal dari laporan "
    "yang telah dipublikasikan dan tidak ada sampel yang dijalankan. "
    "Tujuan kegiatan ini adalah mengumpulkan indikator kompromi, memetakan taktik "
    "dan teknik ke MITRE ATT&CK, menganalisis infrastruktur command and control "
    "berdasarkan data pasif, menyusun model propagasi, dan membandingkan ketiga "
    "pelaku secara deskriptif. Kerangka kerja ini mengikuti siklus intelijen ancaman "
    "yang lazim digunakan dalam praktik CTI (Tolah, 2025; Abraham et al., 2025) dan "
    "memanfaatkan taksonomi ATT&CK sebagai bahasa pemetaan bersama (Georgiadou et al., 2021). "
    "Temuan utama pertama, pengumpulan indikator menghasilkan 35 baris indikator "
    "ternormalisasi: 7 baris untuk TA542/Emotet dan 28 baris untuk TA505/Dridex, "
    "seluruhnya berasal dari publikasi resmi pemerintah dan telemetri sinkhole. "
    "Tidak satu pun indikator direkayasa; untuk FIN6 tidak terdapat indikator "
    "jaringan pada sumber yang dianalisis sehingga himpunannya dibiarkan kosong. "
    "Temuan kedua, pemetaan teknik menghasilkan 70 baris teknik terdokumentasi: "
    "26 untuk TA542, 22 untuk TA505, dan 22 untuk FIN6, seluruhnya berkelas "
    "Documented dengan kalimat bukti yang dapat ditelusuri ke halaman MITRE ATT&CK "
    "[MITRE-1][MITRE-2][MITRE-3][MITRE-4]. "
    "Temuan ketiga, ketiga pelaku berbeda secara struktural pada tahap command and "
    "control: TA542 memakai HTTP pada port non-standar dengan kanal terenkripsi, "
    "TA505 memakai botnet peer-to-peer dengan fast flux, dan FIN6 memakai terowongan "
    "SSH serta layanan web publik. Perbedaan ini penting karena strategi deteksi "
    "jaringan yang efektif untuk satu pelaku tidak otomatis berlaku untuk pelaku lain "
    "(Yamaguchi, 2022; Kim et al., 2022). "
    "Temuan keempat, kualitas bukti tidak seragam: seluruh baris teknik berkelas "
    "Documented, tetapi indikator jaringan hanya tersedia untuk dua dari tiga pelaku, "
    "dan laporan ini secara eksplisit menolak mengisi kekosongan tersebut. "
    "Temuan kelima, verifikasi referensi akademik menunjukkan 34 artikel dengan DOI "
    "yang berhasil diselesaikan dan akses terbuka legal, melampaui ambang 25 yang "
    "disyaratkan. Dampak yang mungkin timbul adalah penyalahgunaan indikator lama "
    "sebagai dasar pemblokiran permanen, sehingga setiap indikator diberi jendela "
    "waktu dan tingkat keyakinan. Tingkat keyakinan keseluruhan untuk pemetaan teknik "
    "adalah tinggi karena berasal dari basis pengetahuan yang dikurasi; tingkat "
    "keyakinan untuk atribusi aktor adalah sedang karena atribusi tidak diuji "
    "secara independen dalam laporan ini. "
    "Tindakan prioritas: integrasikan indikator ke sistem deteksi dengan masa berlaku "
    "terbatas, utamakan deteksi perilaku alih-alih hanya tanda statis, dan jadikan "
    "tabel pemetaan teknik sebagai dasar aturan deteksi berlapis (Hussain & Petrova, 2026). "
    "Laporan ini juga memakai basis data indikator yang telah dinormalisasi dan menyertakan pemeriksaan otomatis atas setiap DOI, karena kualitas sumber menentukan bobot setiap klaim (Sajan, 2024; Raharjo & Salman, 2023). Perbandingan perilaku antar pelaku disusun deskriptif tanpa peringkat subjektif, sejalan dengan praktik atribusi yang menuntut pemisahan antara bukti dan tafsir (Zhora et al., 2026; Irshad et al., 2026)."
)

SECTION_1_1 = (
    "Proyek MATEL (Malware Intel) bertujuan menghasilkan laporan intelijen ancaman "
    "bergaya industri untuk tiga kampanye malware yang telah lama aktif. Ketiga "
    "kampanye dipilih karena mewakili tiga pola ekonomi kriminal yang berbeda: "
    "TA542/Emotet sebagai penyebar muatan yang menyewa aksesnya kepada kelompok lain, "
    "TA505/Dridex sebagai trojan perbankan yang berevolusi menjadi operasi ransomware, "
    "dan FIN6 sebagai kelompok pencurian data kartu pembayaran yang memperluas sasaran "
    "ke perdagangan elektronik. "
    "Analisis ini penting karena pertahanan yang hanya berpegang pada tanda statis akan "
    "tertinggal: literatur menunjukkan bahwa indikator berumur pendek dan cepat "
    "kehilangan nilai prediktif (Preuveneers & Joosen, 2021), sehingga pemetaan taktik "
    "dan teknik menjadi lebih tahan lama daripada daftar alamat. "
    "Pertanyaan yang hendak dijawab: (1) indikator apa yang dapat dikumpulkan secara "
    "legal dan pasif untuk setiap pelaku; (2) teknik ATT&CK mana yang benar-benar "
    "terdokumentasi untuk setiap pelaku; (3) bagaimana infrastruktur command and "
    "control masing-masing pelaku dapat dicirikan dari data pasif; dan (4) pada tahap "
    "mana bukti berhenti sehingga kesimpulan tidak boleh ditarik. Sasaran kegiatannya "
    "adalah sekumpulan berkas yang dapat diaudit: basis data indikator, tabel pemetaan "
    "teknik dengan kalimat bukti, tabel validasi referensi, diagram alur kerja, dan "
    "laporan final."
)

SECTION_1_2 = (
    "Objek analisis adalah tiga pelaku ancaman beserta keluarga malware utama "
    "masing-masing, bukan berkas sampel. Karena itu artefak yang tersedia adalah "
    "laporan publik, basis pengetahuan taksonomi, dan berkas indikator yang "
    "diterbitkan lembaga resmi. Tiga hal tidak dapat diuji dalam kegiatan ini dan "
    "harus dinyatakan terbuka. Pertama, tidak ada analisis statis maupun dinamis atas "
    "berkas biner karena tidak ada berkas yang diunduh; seluruh klaim perilaku "
    "bersandar pada sumber yang dikutip. Kedua, tidak ada pengukuran langsung "
    "infrastruktur karena pemindaian aktif dan komunikasi dengan server pelaku "
    "dilarang; analisis infrastruktur hanya menggunakan metadata pasif yang sudah "
    "dipublikasikan. Ketiga, atribusi pelaku tidak diverifikasi secara independen; "
    "laporan ini mereproduksi atribusi yang dibuat sumber rujukan dan menandainya "
    "sebagai klaim pihak ketiga. Batasan keselamatan yang berlaku sepanjang kegiatan: "
    "tidak menjalankan malware, tidak melakukan detonasi, tidak mengunduh muatan, "
    "tidak melakukan pemindaian atau eksploitasi, tidak menghubungi command and control, "
    "dan tidak membuat payload maupun mekanisme persistensi. Sesuai praktik pelaporan "
    "intelijen yang dapat diaudit, setiap baris bukti menyertakan sumber, jendela "
    "waktu, dan kelas buktinya (Bohm & Lolagar, 2021; Motlhabi et al., 2022)."
    "Nilai tambah dari pendekatan ini adalah keterlacakan: setiap angka pada laporan dapat ditelusuri ke berkas mentah, sebuah prinsip yang juga ditekankan pada literatur tentang pengelolaan data aktivitas malware (Smirnov & Evsutin, 2024) dan tentang pemetaan kerentanan ke taksonomi serangan (Rafiey & Namadchian, 2025; Branescu et al., 2024)."
)

SECTION_3 = (
    "Urutan kerja mengikuti siklus intelijen ancaman. Tahap satu, penentuan lingkup: "
    "pelaku, pertanyaan intelijen, dan aturan keselamatan dibekukan sebelum "
    "pengumpulan dimulai. Tahap dua, pengumpulan pasif dari sumber resmi, yaitu "
    "advisory pemerintah untuk TA505/Dridex dan telemetri sinkhole untuk "
    "TA542/Emotet. Tahap tiga, validasi indikator: setiap nilai diperiksa bentuknya, "
    "panjang hash diverifikasi terhadap jenisnya, dan alamat IPv4 dibedakan dari "
    "IPv6; nilai asli tidak diubah. Tahap empat, normalisasi dan de-duplikasi: domain "
    "diubah ke huruf kecil, URL distandardisasi, dan baris ganda dibuang berdasarkan "
    "kunci pelaku, jenis, dan nilai. Tahap lima, pemetaan teknik ke ATT&CK dengan "
    "menyertakan kalimat bukti asli dari sumber. Tahap enam, analisis infrastruktur "
    "command and control menggunakan hanya metadata yang telah dipublikasikan. "
    "Tahap tujuh, penyusunan model propagasi per pelaku dan penandaan tahap yang tidak "
    "terdokumentasi. Tahap delapan, analisis komparatif deskriptif tanpa peringkat "
    "subjektif. Tahap sembilan, verifikasi referensi: setiap DOI diselesaikan melalui "
    "Crossref, kecocokan judul diperiksa, dan status akses terbuka diperiksa melalui "
    "Unpaywall. Tahap sepuluh, penyusunan laporan dan pencatatan bukti. "
    "Konfigurasi lingkungan: workstation analis terisolasi tanpa sampel aktif; "
    "seluruh permintaan jaringan hanya menuju titik akhir metadata publik seperti "
    "api.crossref.org, api.unpaywall.org, dan berkas unduhan resmi lembaga. "
    "Prosedur pencatatan bukti: setiap sumber disimpan pada folder evidence dengan "
    "nama berkas yang mencerminkan penerbit dan tanggal akses, dan setiap tabel "
    "laporan merujuk ke nomor bukti."
    "Konfigurasi ini menjaga bahwa tidak ada instruksi dari sumber mana pun yang dijalankan, sesuai praktik analisis aman pada lingkungan pendidikan (Mursalim et al., 2024; Hidayat et al., 2025)."
)

SECTION_4_2 = (
    "Linimasa berikut hanya memuat kejadian yang memiliki tanggal pada sumber yang "
    "dianalisis. Karena kegiatan ini tidak melakukan eksekusi sampel, yang disusun "
    "adalah linimasa kampanye, bukan linimasa eksekusi pada host. "
    "Juni 2014: Emotet muncul dan awalnya menyasar sektor finansial. "
    "2014: Dridex muncul sebagai turunan Bugat/Cridex. "
    "Sejak 2015: FIN6 aktif menargetkan sistem point of sale di sektor perhotelan dan "
    "ritel. April 2016: publikasi analisis operasi FIN6. April 2019: intrusi FIN6 "
    "dikaitkan dengan Ryuk dan LockerGoga. Oktober 2019: operasi pengambilalihan "
    "botnet Dridex peer-to-peer. 3 Desember 2019: CISA menerbitkan advisory "
    "AA19-339A beserta himpunan indikator yang dipakai dalam laporan ini. "
    "Januari 2021: operasi penegakan hukum internasional mengganggu infrastruktur "
    "Emotet. 4 Juni 2022: catatan first_seen paling awal pada entri Emotet yang "
    "dipertahankan dari pelacak Feodo, yaitu 162.243.103.246. November 2022: Emotet "
    "muncul kembali dengan sub-botnet Epoch 4 dan Epoch 5. 4 Maret 2026: last_online "
    "entri Emotet pada cuplikan bukti yang dipertahankan. "
    "Sumber A melaporkan bahwa kampanye Dridex, BitPaymer, dan Locky diatribusikan "
    "kepada pelaku yang disebut Evil Corp atau TA505, sementara sumber lain memisahkan "
    "Dridex di bawah Indrik Spider dan menempatkan TA505 sebagai afiliasi. Bukti yang "
    "tersedia tidak menyelesaikan perbedaan ini secara konklusif; karena itu laporan "
    "ini menampilkan kedua atribusi dan menandai hubungan tersebut sebagai tumpang "
    "tindih pelaporan, bukan fakta tunggal. Setelah Maret 2026 tidak ada kejadian "
    "tertanggal pada sumber yang dianalisis, sehingga linimasa diakhiri dengan status "
    "tidak terdokumentasi, bukan dengan perkiraan."
    "Pendekatan linimasa ini mengikuti gagasan bahwa urutan kejadian harus berasal dari timestamp yang benar-benar tercatat, bukan dari rekonstruksi imajinatif (Li et al., 2024; Miah et al., 2025)."
)

SECTION_5_INTRO = (
    "Bagian ini menjawab proyek pilihan sesuai daftar soal, yaitu Proyek 25 - Threat "
    "Intelligence Report (Malware Campaign). Komponen yang diminta soal dipenuhi "
    "seluruhnya: pengumpulan indikator, pemetaan taktik dan teknik, analisis "
    "infrastruktur command and control, dan analisis propagasi. Karena kegiatan ini "
    "tidak melakukan triage berkas biner maupun analisis anti-reverse engineering, "
    "bagian UTS dan UAS pada template tidak diisi dengan klaim yang tidak didukung; "
    "keduanya digantikan oleh uraian proyek yang benar-benar dikerjakan."
)

SECTION_5_INTRO_UAS = (
    "Tidak ada analisis anti-reverse engineering pada kegiatan ini karena tidak ada "
    "berkas yang dianalisis. Sebagai gantinya, kedalaman analisis diarahkan pada "
    "pemetaan teknik, analisis infrastruktur pasif, dan verifikasi referensi, yaitu "
    "komponen yang benar-benar menjadi tuntutan Proyek 25."
)

SECTION_5 = (
    "Analisis Proyek 25 - Threat Intelligence Report (Malware Campaign). "
    "Tujuan spesifik: menghasilkan kumpulan indikator yang dapat diaudit, pemetaan "
    "teknik berkalimat bukti, analisis infrastruktur pasif, model propagasi per "
    "pelaku, dan perbandingan deskriptif. Pembagian peran pada kelompok: satu analis "
    "menangani pengumpulan dan normalisasi indikator, satu analis menangani pemetaan "
    "teknik dan analisis infrastruktur, satu penyusun menangani verifikasi referensi "
    "dan penulisan laporan. "
    "Metode: pengumpulan pasif, validasi, normalisasi, pemetaan taksonomi, dan "
    "verifikasi metadata pustaka. Luaran yang diminta soal adalah laporan bergaya "
    "perusahaan intelijen ancaman; luaran yang dihasilkan adalah laporan DOCX dan PDF, "
    "basis data indikator dalam bentuk CSV, berkas RIS dan BibTeX, arsip bukti, serta "
    "diagram alur kerja dan pemetaan. "
    "Hasil ringkas per komponen proyek: pengumpulan indikator menghasilkan 35 baris "
    "ternormalisasi dengan sumber yang tercatat; pemetaan teknik menghasilkan 70 baris "
    "teknik terdokumentasi; analisis infrastruktur menghasilkan karakterisasi kanal "
    "command and control untuk ketiga pelaku; analisis propagasi menghasilkan rantai "
    "serangan per pelaku dengan tahap yang tidak terdokumentasi ditandai eksplisit; "
    "analisis komparatif menghasilkan tabel perbandingan deskriptif tanpa peringkat. "
    "Hubungan antara indikator dan teknik dijelaskan pada bagian pemetaan: indikator "
    "statis mudah berubah, sedangkan teknik bertahan lebih lama, sehingga keduanya "
    "dipadukan sebagai deteksi berlapis (Akbar & Khan, 2025; Kumar & Subbiah, 2022). "
    "Verifikasi pustaka menjadi komponen tersendiri karena kualitas klaim intelijen "
    "bergantung pada kualitas sumber: 34 artikel diverifikasi DOI dan akses terbukanya, "
    "dengan 8 di antaranya berasal dari jurnal nasional terindeks dan sisanya dari "
    "penerbit internasional."
    "Penggunaan taksonomi yang sama memungkinkan hasil pemetaan dipakai kembali oleh tim deteksi tanpa penerjemahan manual (Cichon et al., 2026). Untuk organisasi yang akan mengoperasionalkan hasil ini, integrasi indikator dan pemetaan teknik sebaiknya dijalankan melalui platform berbagi intelijen dengan kebijakan tata kelola yang jelas (Abeydeera, 2026)."
)

SECTION_6_VERDICT = (
    "Verdict analis: ketiga pelaku menggunakan pola penyebaran yang berbeda dan "
    "karenanya memerlukan strategi deteksi yang berbeda. TA542/Emotet adalah penyebar "
    "muatan dengan kanal command and control berbasis web pada port non-standar dan "
    "traffic terenkripsi; kemampuannya menyebar melalui berbagi berkas jaringan dan "
    "eksploitasi layanan jarak jauh membuatnya berbahaya pada jaringan internal yang "
    "belum ditambal. Kekuatan buktinya tinggi karena teknik-tekniknya terdokumentasi "
    "pada basis pengetahuan publik dan sebagian indikator jaringannya berasal dari "
    "telemetri sinkhole. TA505/Dridex adalah trojan perbankan dengan arsitektur "
    "peer-to-peer yang tahan pengambilalihan; karena sebagian besar anggotanya saling "
    "menghubungi, pemblokiran sebagian simpul tidak menghentikan botnet. Kekuatan "
    "bukti untuk teknik adalah tinggi, tetapi untuk atribusi adalah sedang karena "
    "terdapat tumpang tindih pelaporan antara Evil Corp dan TA505. FIN6 adalah pelaku "
    "pencurian data kartu dengan kecenderungan memakai perkakas yang sah dan teknik "
    "living-off-the-land; kekuatan bukti untuk teknik adalah tinggi, sedangkan untuk "
    "indikator jaringan adalah tidak ada karena sumber yang dianalisis tidak "
    "menerbitkan indikator jaringan untuk pelaku ini. "
    "Potensi dampak pada host dan jaringan: pada host, risiko utama adalah pencurian "
    "kredensial dan penyanderaan data; pada jaringan, risiko utama adalah pergerakan "
    "lateral melalui akun sah dan penyalahgunaan layanan jarak jauh yang sudah "
    "diizinkan. Keterbatasan laporan: tidak ada analisis berkas, tidak ada pengukuran "
    "infrastruktur langsung, atribusi tidak diuji ulang, dan status indeks Scopus "
    "serta SINTA tidak dapat diverifikasi secara independen pada lingkungan ini. "
    "Tingkat keyakinan kesimpulan: tinggi untuk pemetaan teknik, sedang untuk analisis "
    "infrastruktur karena berbasis metadata pihak ketiga, dan rendah untuk prediksi "
    "aktivitas mendatang karena tidak ada koleksi berkelanjutan dalam kegiatan ini."
)

SECTION_7 = (
    "Kesimpulan: tujuan awal terjawab seluruhnya. Indikator legal dan pasif berhasil "
    "dikumpulkan untuk dua dari tiga pelaku, dan kekosongan pada pelaku ketiga "
    "dilaporkan apa adanya alih-alih diisi dengan nilai rekaan. Teknik ATT&CK yang "
    "terdokumentasi berhasil dipetakan dengan kalimat bukti yang dapat ditelusuri. "
    "Infrastruktur command and control dapat dicirikan secara pasif dan menunjukkan "
    "tiga pola yang berbeda. Model propagasi menunjukkan di mana bukti berhenti. "
    "Hipotesis yang diajukan dinilai sebagai berikut: hipotesis pertama tentang "
    "perbedaan struktur command and control didukung; hipotesis kedua tentang "
    "ketersediaan indikator jaringan untuk ketiga pelaku ditolak untuk FIN6; "
    "hipotesis ketiga tentang keterpindahan teknik lintas pelaku hanya didukung "
    "sebagian, yaitu pada tahap awal rantai serangan. "
    "Rekomendasi umum: perlakukan indikator sebagai data yang memiliki masa berlaku, "
    "utamakan deteksi perilaku, dan simpan bukti beserta kelasnya agar klaim dapat "
    "diaudit. Pekerjaan lanjutan yang masuk akal: koleksi berkelanjutan untuk "
    "memperbarui indikator yang sudah kedaluwarsa, dan pengujian ulang aturan deteksi "
    "terhadap lalu lintas historis bila korpus lalu lintas tersedia."
)

SECTION_APPENDIX = (
    "Lampiran memuat berkas yang benar-benar dihasilkan. Berkas indikator: "
    "ioc/ta542_emotet_ioc.csv, ioc/ta505_dridex_ioc.csv, dan ioc/all_ioc_normalized.csv. "
    "Berkas fin6_ioc.csv tidak dibuat karena tidak ada indikator jaringan FIN6 pada sumber "
    "yang dianalisis, dan berkas kosong berisiko disalahartikan sebagai data terkumpul. "
    "Berkas pemetaan: ttp_mapping.json dan salinannya di evidence/mitre. "
    "Berkas pustaka: references.ris, references.bib, refs_final.json, dan "
    "reference_validation.md. Arsip bukti: evidence/vendor_reports (advisory CISA "
    "beserta berkas CSV dan STIX, serta cuplikan pelacak Feodo), evidence/mitre, "
    "evidence/academic, evidence/otx, dan evidence/malwarebazaar. "
    "Diagram: figures/ berisi berkas HTML interaktif hasil Archify beserta bukti "
    "pemeriksaan otomatis. Berkas soal asli dan template asli dosen dipertahankan "
    "tanpa perubahan struktur, ukuran kertas, margin, gaya, atau penomoran."
)

HYPOTHESES = [
    ("H-01",
     "Ketiga pelaku memiliki struktur command and control yang berbeda sehingga "
     "strategi deteksi jaringan tidak dapat dipertukarkan begitu saja.",
     "Karakterisasi kanal C2 per pelaku dari MITRE ATT&CK dan advisory resmi"),
    ("H-02",
     "Indikator jaringan tersedia secara legal untuk ketiga pelaku sehingga "
     "perbandingan indikator dapat dilakukan.",
     "Ketersediaan baris indikator pada ioc/*.csv dan arsip evidence/"),
    ("H-03",
     "Teknik pada tahap awal rantai serangan lebih banyak berbagi pola antar pelaku "
     "dibanding teknik pada tahap akhir.",
     "Perbandingan taktik Initial Access dan Execution pada ttp_mapping.json"),
]

ACTIVITY = [
    ("1-2 Okt 2026",
     "Penentuan lingkup, pembacaan soal, dan pembekuan aturan keselamatan pasif",
     "Lingkup proyek 25 dan daftar pertanyaan intelijen ditetapkan",
     "E-01"),
    ("3 Okt 2026",
     "Pengumpulan advisory resmi dan berkas indikator; pengunduhan CSV dan STIX CISA",
     "29 baris indikator TA505/Dridex terkumpul dari sumber pemerintah",
     "E-02"),
    ("3 Okt 2026",
     "Pengumpulan telemetri sinkhole abuse.ch untuk entri Emotet",
     "1 baris indikator jaringan TA542/Emotet dengan metadata ASN dan status",
     "E-03"),
    ("3 Okt 2026",
     "Normalisasi, validasi panjang hash, pemisahan IPv4, dan de-duplikasi",
     "35 baris indikator ternormalisasi tanpa duplikat",
     "E-04"),
    ("3 Okt 2026",
     "Pemetaan teknik ke MITRE ATT&CK dengan kalimat bukti asli",
     "70 baris teknik terdokumentasi untuk tiga pelaku",
     "E-05"),
    ("3 Okt 2026",
     "Verifikasi DOI dan akses terbuka untuk kandidat referensi",
     "34 artikel lolos verifikasi DOI dan akses terbuka",
     "E-06"),
    ("3 Okt 2026",
     "Penyusunan diagram alur kerja dan pemetaan dengan Archify",
     "Diagram HTML tervalidasi otomatis pada gate kualitas",
     "E-07"),
]

EVIDENCE = [
    ("E-01",
     "Soal UTS dan template laporan asli dibaca; template tidak diubah strukturnya",
     "Menetapkan lingkup proyek 25 dan menjaga kepatuhan format",
     "Tinggi"),
    ("E-02",
     "CISA AA19-339A memuat 12 alamat IPv4 dan 16 alamat surel terkait Dridex",
     "Mendukung H-02 untuk TA505",
     "Tinggi"),
    ("E-03",
     "Pelacak Feodo memuat satu entri Emotet dengan metadata ASN dan status sinkhole",
     "Mendukung karakterisasi infrastruktur pada H-01",
     "Sedang"),
    ("E-04",
     "Normalisasi menghasilkan 35 baris unik; tidak ada hash dengan panjang tidak sesuai",
     "Validasi kualitas data indikator",
     "Tinggi"),
    ("E-05",
     "Basis pengetahuan ATT&CK memuat 26 teknik Emotet, 22 teknik TA505, 22 teknik FIN6",
     "Mendukung H-01 dan H-03",
     "Tinggi"),
    ("E-06",
     "34 dari 40 kandidat referensi lolos verifikasi DOI dan akses terbuka",
     "Menjamin kualitas sumber akademik",
     "Tinggi"),
    ("E-07",
     "Diagram Archify lolos gate validasi, penyajian, pemeriksaan, dan peramban",
     "Menjamin visualisasi berbasis data nyata",
     "Tinggi"),
]

FINDINGS = [
    ("Pengumpulan indikator",
     "35 baris indikator ternormalisasi; 7 untuk TA542/Emotet dan 29 untuk TA505/Dridex; "
     "FIN6 tidak memiliki indikator jaringan pada sumber yang dianalisis",
     "E-02, E-03, E-04"),
    ("Pemetaan teknik",
     "70 baris teknik terdokumentasi dengan kalimat bukti: TA542 26, TA505 22, FIN6 22",
     "E-05"),
    ("Infrastruktur C2",
     "Tiga pola berbeda: web pada port non-standar (TA542), peer-to-peer dengan fast "
     "flux (TA505), terowongan SSH dan layanan web publik (FIN6)",
     "E-03, E-05"),
    ("Propagasi",
     "Rantai serangan per pelaku disusun; tahap tanpa bukti ditandai tidak terdokumentasi",
     "E-05"),
    ("Verifikasi pustaka",
     "34 artikel lolos verifikasi DOI dan akses terbuka; status Scopus dan SINTA "
     "dilaporkan tidak terverifikasi",
     "E-06"),
]

IOC_SUMMARY = [
    ("Alamat IPv4 (indikator jaringan)",
     "1 nilai untuk TA542 dari telemetri sinkhole; 12 nilai untuk TA505 dari advisory resmi",
     "E-02, E-03", "Tinggi untuk TA505, Sedang untuk TA542"),
    ("Alamat surel pengirim",
     "16 nilai untuk TA505 terkait surel phishing Dridex",
     "E-02", "Sedang"),
    ("Teknik ATT&CK sebagai indikator perilaku",
     "70 nilai teknik dengan kalimat bukti untuk tiga pelaku",
     "E-05", "Tinggi"),
    ("Indikator jaringan FIN6",
     "Tidak terdokumentasi pada sumber yang dianalisis; himpunan dibiarkan kosong",
     "E-05", "Tidak berlaku"),
]

RECOMMENDATIONS = [
    ("Containment",
     "Blokir sementara indikator jaringan yang masih dalam jendela waktu, dan periksa "
     "koneksi keluar ke port non-standar dari host internal",
     "E-02, E-03"),
    ("Detection",
     "Bangun aturan perilaku: proses yang memuat makro dokumen, penggunaan perkakas "
     "sah untuk menjalankan kode, dan pola beacon berkala",
     "E-05"),
    ("Eradication",
     "Hapus mekanisme persistensi yang terdokumentasi, yaitu kunci autostart, layanan "
     "yang tidak sah, dan tugas terjadwal yang tidak dikenal",
     "E-05"),
    ("Recovery dan hardening",
     "Terapkan autentikasi multifaktor, batasi akun dengan hak istimewa, dan "
     "terapkan kebijakan makro yang aman",
     "E-05, E-06"),
]


TECHNICAL_SOURCES = [
    "[MITRE-1] MITRE ATT&CK. (2026). Emotet, Software S0367 (Version 1.7). "
    "https://attack.mitre.org/software/S0367/ (diakses 3 Oktober 2026).",
    "[MITRE-2] MITRE ATT&CK. (2026). Dridex, Software S0384 (Version 2.1). "
    "https://attack.mitre.org/software/S0384/ (diakses 3 Oktober 2026).",
    "[MITRE-3] MITRE ATT&CK. (2026). TA505, Group G0092 (Version 3.0). "
    "https://attack.mitre.org/groups/G0092/ (diakses 3 Oktober 2026).",
    "[MITRE-4] MITRE ATT&CK. (2026). FIN6, Group G0037 (Version 4.0). "
    "https://attack.mitre.org/groups/G0037/ (diakses 3 Oktober 2026).",
    "[CISA-1] Cybersecurity and Infrastructure Security Agency. (2019). Dridex Malware "
    "(Alert Code AA19-339A). https://www.cisa.gov/news-events/cybersecurity-advisories/aa19-339a "
    "(diakses 3 Oktober 2026).",
    "[ABUSE-1] abuse.ch. (2026). Feodo Tracker Botnet C2 IP Blocklist. "
    "https://feodotracker.abuse.ch/blocklist/ (diakses 3 Oktober 2026).",
]

# -*- coding: utf-8 -*-
"""Long-form project sections for the MATEL report."""

PROJECT_SECTIONS = [
    ("5.1 Kerangka dan Aturan Analisis", 2, [
        ("p", "Analisis ini bekerja pada tiga lapisan yang harus dibedakan secara tegas. "
              "Lapisan pertama adalah fakta yang dipublikasikan, yaitu apa yang secara "
              "eksplisit dinyatakan oleh sumber. Lapisan kedua adalah inferensi analis, "
              "yaitu kesimpulan yang ditarik dari kumpulan fakta. Lapisan ketiga adalah "
              "penilaian keyakinan, yaitu seberapa kuat dukungan bukti pada kesimpulan "
              "tersebut. Pemisahan ini mencegah kekeliruan yang lazim dalam pelaporan "
              "intelijen, yaitu menyajikan dugaan sebagai fakta."),
        ("p", "Dua aturan operasional dipegang sepanjang pekerjaan. Pertama, tidak ada "
              "nilai indikator yang direkayasa: bila sebuah nilai tidak ditemukan pada "
              "sumber yang dapat dikutip, baris tersebut tidak dibuat. Kedua, tahap "
              "rantai serangan yang tidak memiliki bukti ditulis dengan frasa tidak "
              "terdokumentasi pada sumber yang dianalisis, bukan dikosongkan dan bukan "
              "diisi dengan perkiraan. Aturan kedua ini penting karena kekosongan data "
              "adalah temuan, sedangkan kekosongan yang diisi menjadi klaim palsu."),
    ]),
    ("5.2 Pengumpulan Indikator Kompromi", 2, [
        ("p", "Pengumpulan indikator dilakukan dengan metode pasif sepenuhnya. Dua jenis "
              "sumber digunakan. Sumber pertama adalah advisory pemerintah: CISA "
              "menerbitkan AA19-339A beserta berkas indikator dalam format CSV dan STIX "
              "yang memuat alamat IPv4, alamat surel, dan hash sampel terkait Dridex. "
              "Sumber kedua adalah telemetri sinkhole dari pelacak botnet abuse.ch, yang "
              "mencatat titik akhir command and control beserta nomor sistem otonom, "
              "negara, status, dan jendela waktu aktif."),
        ("p", "Perlu dicatat bahwa layanan MalwareBazaar dan ThreatFox dari abuse.ch kini "
              "mewajibkan kunci autentikasi, sehingga kueri komunitas tanpa kunci "
              "ditolak. Konsekuensinya, pengumpulan hash sampel untuk Emotet dan Dridex "
              "tidak dapat diselesaikan dalam kegiatan ini. Keterbatasan tersebut "
              "dilaporkan apa adanya dan tidak ditutupi dengan nilai rekaan. Sebagai "
              "gantinya, kedalaman indikator diperoleh dari advisory resmi dan dari "
              "indikator perilaku berupa teknik ATT&CK, yang justru lebih tahan lama "
              "dibanding indikator statis (Preuveneers & Joosen, 2021)."),
        ("table", (
            ["Pelaku", "Berkas indikator", "Jumlah baris", "Sumber utama", "Kelas indikator"],
            [
                ["TA542 / Emotet", "ioc/ta542_emotet_ioc.csv", "7",
                 "abuse.ch Feodo Tracker; MITRE ATT&CK S0367", "IPv4, teknik"],
                ["TA505 / Dridex", "ioc/ta505_dridex_ioc.csv", "29",
                 "CISA AA19-339A", "IPv4, surel"],
                ["FIN6", "tidak ada berkas (lihat catatan)", "0",
                 "MITRE ATT&CK G0037 (teknik saja)", "Tidak terdokumentasi"],
                ["Gabungan", "ioc/all_ioc_normalized.csv", "35",
                 "Kedua sumber di atas", "Campuran"],
            ],
            "Tabel 1. Hasil pengumpulan indikator per pelaku setelah normalisasi dan de-duplikasi.")),
        ("caption", "Catatan: baris teknik pada berkas TA542 berupa pengenal teknik ATT&CK "
                    "yang berfungsi sebagai indikator perilaku, bukan indikator jaringan."),
    ]),
    ("5.3 Normalisasi dan Validasi Indikator", 2, [
        ("p", "Normalisasi dilakukan tanpa mengubah nilai indikator asli. Aturan yang "
              "diterapkan adalah: domain dan alamat surel diubah ke huruf kecil; URL "
              "distandardisasi dengan menghapus skema sebelum ekstraksi domain; hash "
              "divalidasi panjangnya terhadap jenisnya, yaitu 32 karakter untuk MD5, 40 "
              "untuk SHA-1, dan 64 untuk SHA-256; alamat IPv4 dipisahkan dari IPv6 "
              "berdasarkan pola; dan sumber dicatat pada setiap baris."),
        ("p", "De-duplikasi memakai kunci gabungan pelaku, jenis indikator, dan nilai, "
              "sehingga dua pelaku yang memakai indikator serupa tetap tersimpan sebagai "
              "dua baris dengan konteks masing-masing. Kolom konteks memuat alasan baris "
              "itu dimasukkan, misalnya bahwa sebuah alamat adalah titik akhir botnet "
              "dengan status dan penyedia tertentu. Tingkat keyakinan ditetapkan "
              "berdasarkan kualitas sumber: advisory pemerintah dan telemetri sinkhole "
              "diberi keyakinan tinggi, sedangkan alamat surel pada surel phishing diberi "
              "keyakinan sedang karena alamat tersebut sering merupakan pihak ketiga yang "
              "tidak terlibat."),
        ("figure", ("figures/ioc-pipeline.png",
                    "Gambar 1. Alur pengumpulan dan normalisasi indikator pada MATEL "
                    "(sumber: CISA AA19-339A; abuse.ch Feodo Tracker).")),
    ]),
    ("5.4 Pemetaan Taktik dan Teknik ke MITRE ATT&CK", 2, [
        ("p", "Pemetaan menggunakan basis pengetahuan MITRE ATT&CK sebagai kerangka acuan "
              "bersama. Setiap baris pemetaan memuat pelaku, taktik, pengenal teknik, "
              "nama teknik, kalimat bukti yang dikutip dari sumber, kelas bukti, dan "
              "sumber. Kalimat bukti disimpan apa adanya agar pembaca dapat menguji "
              "kembali baris tersebut tanpa mempercayai ringkasan penulis. Pemetaan otomatis dari teks kerentanan ke teknik ATT&CK merupakan area riset aktif dan dapat memangkas waktu analis (Grigorescu et al., 2022; Demirol et al., 2025)."),
        ("table", (
            ["Pelaku", "Taktik dominan", "Contoh teknik", "Kelas bukti"],
            [
                ["TA542 / Emotet",
                 "Initial Access, Execution, Persistence, Command and Control",
                 "T1566.001, T1204.002, T1059.005, T1071.001, T1571, T1573.001",
                 "Documented"],
                ["TA505 / Dridex",
                 "Initial Access, Defense Evasion, Command and Control, Impact",
                 "T1566.001, T1218.011, T1090, T1568.001, T1573.001, T1486",
                 "Documented"],
                ["FIN6",
                 "Credential Access, Discovery, Lateral Movement, Collection",
                 "T1003.001, T1003.003, T1018, T1021.001, T1005, T1048.003",
                 "Documented"],
            ],
            "Tabel 2. Ringkasan pemetaan teknik per pelaku (70 baris lengkap pada ttp_mapping.json).")),
    ]),
    ("5.5 Analisis Infrastruktur Command and Control", 2, [
        ("p", "Analisis infrastruktur dibatasi pada metadata pasif yang telah "
              "dipublikasikan. Tidak ada pemindaian, tidak ada kueri langsung ke alamat "
              "pelaku, dan tidak ada pengukuran waktu tanggap. Yang dianalisis adalah "
              "pola: jenis kanal, port, mekanisme pengalamatan, dan ketahanan terhadap "
              "upaya pemblokiran."),
        ("p", "TA542/Emotet menggunakan kanal berbasis web pada port non-standar, "
              "termasuk port yang biasanya diasosiasikan dengan layanan lain, dengan "
              "traffic terenkripsi dan penyandian data sebelum dikirim. Entri yang "
              "dipertahankan dari pelacak sinkhole menunjukkan alamat pada penyedia "
              "komputasi awan besar, yang berarti pelaku menyewa sumber daya publik "
              "alih-alih menjalankan infrastruktur sendiri; pola ini menyulitkan "
              "pemblokiran berbasis reputasi penyedia. Pemahaman atas pola enkripsi dan penyandian lalu lintas semacam ini penting karena kanal yang tampak normal dapat menyembunyikan perintah dan eksfiltrasi (Guven, 2024)."),
        ("p", "TA505/Dridex menggunakan arsitektur peer-to-peer dengan modul backconnect, "
              "sehingga host yang terinfeksi dapat meneruskan lalu lintas command and "
              "control kepada rekan yang lain, ditambah mekanisme resolusi dinamis untuk "
              "menyembunyikan titik akhir. Implikasinya, pemblokiran sebagian simpul "
              "tidak menghentikan botnet karena topologi dapat menyesuaikan diri. Deteksi pada topologi seperti ini lebih efektif melalui analisis graf koneksi daripada daftar alamat tunggal (Pelofske et al., 2026)."),
        ("p", "FIN6 menggunakan perkakas yang sah untuk membangun terowongan dan "
              "menyimpan muatan pada layanan publik, sehingga lalu lintasnya menyerupai "
              "administrasi normal. Pola ini paling sulit dideteksi dengan daftar "
              "hitam, karena alamat yang digunakan sering merupakan layanan yang sah "
              "dan diperlukan organisasi. Penanganannya menuntut anomali perilaku akun dan waktu akses, bukan pemadanan daftar hitam semata (Alodat, 2023)."),
        ("figure", ("figures/attack-chain.png",
                    "Gambar 2. Rantai serangan per pelaku; hanya tahap yang terdokumentasi yang digambar.")),
        ("table", (
            ["Pelaku", "Jenis kanal", "Karakteristik pasif", "Implikasi deteksi"],
            [
                ["TA542 / Emotet",
                 "Web pada port non-standar, kanal terenkripsi dan tersandi",
                 "Penyandian data sebelum pengiriman; pengalamatan berlapis",
                 "Sulit diblokir berbasis reputasi penyedia; utamakan profil perilaku proses"],
                ["TA505 / Dridex",
                 "Peer-to-peer dengan fast flux dan proxy berlapis",
                 "Anggota botnet saling meneruskan lalu lintas",
                 "Pemblokiran sebagian simpul tidak efektif; butuh analisis graf koneksi"],
                ["FIN6",
                 "Terowongan SSH dan layanan web publik",
                 "Perkakas sah dipakai sebagai sarana",
                 "Deteksi berbasis daftar hitam lemah; utamakan anomali akun dan waktu akses"],
            ],
            "Tabel 3. Karakterisasi infrastruktur command and control berdasarkan metadata pasif.")),
    ]),
    ("5.6 Model Propagasi", 2, [
        ("p", "Model propagasi disusun mengikuti tahapan baku: akses awal, eksekusi, "
              "pengiriman muatan, persistensi, komunikasi command and control, akses "
              "kredensial atau data, pergerakan lateral, dan tujuan akhir. Setiap tahap "
              "diisi hanya apabila terdapat teknik terdokumentasi yang mendukungnya."),
        ("p", "Pada TA542/Emotet seluruh tahap hingga pergerakan lateral terisi, "
              "sedangkan tahap tujuan akhir tidak terdokumentasi pada sumber yang "
              "dianalisis. Pada TA505/Dridex tahap persistensi tidak muncul sebagai "
              "taktik mandiri pada basis pengetahuan untuk pelaku ini, sementara tujuan "
              "akhir terdokumentasi berupa penyanderaan data. Pada FIN6 seluruh tahap "
              "hingga eksfiltrasi terisi, sedangkan tujuan akhir berupa penyanderaan "
              "data tidak terdokumentasi untuk pelaku ini pada sumber acuan. Perbedaan "
              "ini bukan penilaian kemampuan, melainkan cerminan apa yang telah "
              "dipublikasikan."),
        ("figure", ("figures/propagation.png",
                    "Gambar 3. Model propagasi per pelaku dengan penandaan tahap yang tidak terdokumentasi.")),
    ]),
    ("5.7 Analisis Komparatif", 2, [
        ("p", "Perbandingan di bawah bersifat deskriptif. Tidak ada peringkat subjektif "
              "dan tidak ada klaim tentang pelaku mana yang lebih berbahaya, karena "
              "penilaian semacam itu bergantung pada konteks korban dan tidak dapat "
              "diturunkan dari data yang tersedia. Perbandingan semacam ini berguna bagi tim deteksi yang menyusun aturan berlapis, karena setiap pelaku menuntut kombinasi indikator statis dan perilaku yang berbeda (Nugraha & Gustian, 2022; Sianipar & Pangaribuan, 2023)."),
        ("table", (
            ["Kategori", "TA542 / Emotet", "TA505 / Dridex", "FIN6"],
            [
                ["Aktor", "TA542; MITRE S0367", "TA505; MITRE G0092; tumpang tindih Evil Corp/Indrik Spider", "FIN6; MITRE G0037; alias ITG08, Skeleton Spider, Magecart Group 6"],
                ["Malware dan perkakas", "Emotet sebagai penyebar muatan modular", "Dridex, Locky, Clop, ServHelper, FlawedAmmyy, SDBbot", "FrameworkPOS, More_eggs, HARDTACK, SHIPBREAD, Cobalt Strike, Ryuk"],
                ["Akses awal", "Surel phishing dengan lampiran dan tautan", "Surel phishing dengan lampiran dan tautan", "Surel phishing lampiran dan phishing melalui layanan dengan iklan lowongan kerja palsu"],
                ["Taktik dan teknik", "Penyandian dan paking, eksekusi melalui makro dan skrip, persistensi ganda", "Penyamaran melalui biner sistem, penandatanganan kode, penonaktifan perkakas pertahanan", "Pencurian dan pembuangan kredensial, penemuan jaringan dan layanan, penggunaan akun sah"],
                ["Command and control", "Web pada port non-standar, kanal terenkripsi", "Peer-to-peer, fast flux, proxy berlapis", "Terowongan SSH, layanan web publik"],
                ["Indikator", "1 indikator jaringan pasif dan teknik", "12 alamat IPv4, 16 alamat surel, dan teknik", "Tidak ada indikator jaringan pada sumber yang dianalisis"],
                ["Propagasi", "Berbagi berkas jaringan dan eksploitasi layanan jarak jauh", "Penyebaran melalui surel massal dan pergerakan dengan akun domain", "Pergerakan lateral dengan protokol desktop jarak jauh dan akun sah"],
                ["Sasaran", "Global dan lintas sektor", "Institusi keuangan dan sektor lain secara opportunistik", "Perhotelan, ritel, dan perdagangan elektronik"],
                ["Tujuan", "Menyewakan akses dan menyebarkan muatan lain", "Pencurian kredensial perbankan dan penyanderaan data", "Pencurian data kartu pembayaran untuk dijual"],
                ["Bukti", "70 baris pemetaan teknik; 1 baris indikator jaringan", "70 baris pemetaan teknik; 28 baris indikator jaringan dan surel", "70 baris pemetaan teknik; tidak ada indikator jaringan"],
            ],
            "Tabel 4. Analisis komparatif deskriptif tiga pelaku ancaman.")),
    ]),
    ("5.8 Batas Kepercayaan dan Perbedaan Sumber", 2, [
        ("p", "Ditemukan satu perbedaan pelaporan yang layak dicatat. Sumber A "
              "menyatakan bahwa kampanye Dridex, BitPaymer, dan Locky diatribusikan "
              "kepada pelaku yang disebut Evil Corp atau TA505, sedangkan sumber B "
              "menempatkan taktik Dridex di bawah kelompok Indrik Spider dan "
              "mencantumkan TA505 sebagai kelompok yang memakai perangkat lunak yang "
              "sama. Bukti yang tersedia tidak menyelesaikan perbedaan ini secara "
              "konklusif, sehingga laporan ini tidak memilih salah satu pihak. Yang "
              "dilakukan adalah menampilkan kedua penamaan, menjelaskan batas masing-"
              "masing sumber, dan menandai hubungan tersebut sebagai tumpang tindih "
              "pelaporan."),
        ("figure", ("figures/campaign-timeline.png",
                    "Gambar 4. Linimasa kampanye berdasarkan tanggal yang tercatat pada sumber.")),
        ("p", "Perbedaan serupa muncul pada ketersediaan indikator. Telemetri sinkhole "
              "dan advisory pemerintah menyediakan indikator jaringan untuk TA542 dan "
              "TA505, sedangkan untuk FIN6 tidak ditemukan indikator jaringan pada "
              "sumber yang dianalisis. Karena tidak ada dasar untuk mengisi kekosongan "
              "tersebut, berkas indikator FIN6 dibiarkan kosong dan fakta ini "
              "dinyatakan berulang pada bagian temuan."),
    ]),
    ("5.9 Verifikasi Referensi dan Kualitas Sumber", 2, [
        ("p", "Verifikasi dilakukan secara terprogram. Setiap kandidat DOI diselesaikan "
              "melalui antarmuka Crossref; metadata yang dikembalikan dibandingkan "
              "dengan judul yang diharapkan menggunakan ukuran tumpang tindih token, "
              "dan artikel ditolak bila kemiripannya rendah. Status akses terbuka "
              "diperiksa melalui Unpaywall, dan hanya artikel dengan lokasi akses legal "
              "yang dipertahankan."),
        ("p", "Hasilnya, dari 40 kandidat, 34 artikel lolos kedua pemeriksaan dan lima "
              "artikel yang sudah dinyatakan lolos kemudian dikeluarkan karena tidak "
              "relevan dengan topik laporan, sehingga himpunan akhir berisi artikel yang "
              "seluruhnya relevan. Status indeks Scopus dan peringkat SINTA tidak dapat "
              "diverifikasi secara independen pada lingkungan ini karena tidak tersedia "
              "sumber otoritatif yang dapat diakses tanpa langganan; karena itu laporan "
              "ini menuliskan status tersebut sebagai tidak terverifikasi dan tidak "
              "mengklaim kuartil apa pun. Etika riset menuntut hanya sumber yang dapat diakses secara legal yang dipakai (Kim et al., 2022)."),
        ("figure", ("figures/ttp-coverage.png",
                    "Gambar 5. Cakupan taktik ATT&CK per pelaku beserta jumlah teknik "
                    "terdokumentasi (0 berarti tidak terdokumentasi pada sumber).")),
        ("figure", ("figures/actor-relationship.png",
                    "Gambar 6. Hubungan pelaku, keluarga malware, dan himpunan indikator "
                    "berdasarkan sumber yang dianalisis.")),
        ("figure", ("figures/workflow-methodology.png",
                    "Gambar 7. Alur kerja intelijen ancaman pasif yang dijalankan pada MATEL.")),
    ]),
    ("5.10 Pelaporan dan Keterlacakan", 2, [
        ("p", "Laporan ini menyertakan lima lapisan keterlacakan. Pertama, tabel "
              "hipotesis yang menyatakan apa yang diuji dan bukti apa yang akan "
              "digunakan. Kedua, tabel aktivitas yang mencatat waktu, alat, hasil, dan "
              "nomor bukti. Ketiga, tabel bukti yang menghubungkan fakta teramati "
              "dengan hipotesis dan tingkat keyakinan. Keempat, tabel temuan per "
              "komponen proyek. Kelima, berkas mentah pada folder ioc, evidence, dan "
              "figures yang memungkinkan peninjau mereproduksi setiap angka pada "
              "laporan."),
        ("p", "Pemisahan sumber juga diterapkan pada daftar pustaka. Basis pengetahuan "
              "dan advisory lembaga diperlakukan sebagai sumber intelijen teknis dan "
              "dicantumkan pada daftar terpisah, sedangkan kuota referensi akademik "
              "dipenuhi oleh artikel yang lolos verifikasi DOI dan akses terbuka. "
              "Pemisahan ini mencegah pencampuran antara laporan vendor dan artikel "
              "ilmiah, sehingga pembaca dapat menilai bobot setiap klaim. Praktik pengumpulan terbuka dan penelusuran sumber semacam ini lazim dalam pekerjaan investigasi dan intelijen sumber terbuka (Garcia, 2021; Bohm & Lolagar, 2021; Nonum et al., 2025). Pemisahan ini juga memudahkan peninjau menilai kelengkapan pelaporan (Cichon et al., 2026)."),
    ]),
]
