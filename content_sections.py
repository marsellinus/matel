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
                ["FIN6", "ioc/fin6_ioc.csv", "0",
                 "MITRE ATT&CK G0037 (teknik saja)", "Tidak terdokumentasi"],
                ["Gabungan", "ioc/all_ioc_normalized.csv", "36",
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
                    "Gambar 2. Model propagasi per pelaku dengan penandaan tahap yang tidak terdokumentasi.")),
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
                    "Gambar 3. Linimasa kampanye berdasarkan tanggal yang tercatat pada sumber.")),
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
                    "Gambar 4. Cakupan taktik ATT&CK per pelaku beserta jumlah teknik "
                    "terdokumentasi (0 berarti tidak terdokumentasi pada sumber).")),
        ("figure", ("figures/actor-relationship.png",
                    "Gambar 5. Hubungan pelaku, keluarga malware, dan himpunan indikator "
                    "berdasarkan sumber yang dianalisis.")),
        ("figure", ("figures/workflow-methodology.png",
                    "Gambar 6. Alur kerja intelijen ancaman pasif yang dijalankan pada MATEL.")),
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
