# Student Performance Analyzer

Program terminal Python untuk mempelajari analisis performa akademik menggunakan dataset contoh.

## Tujuan
Mengubah data mentah menjadi ringkasan statistik, visualisasi, dan rekomendasi awal yang dapat ditinjau lebih lanjut.

## Fitur
- Membaca data CSV.
- Memeriksa kolom, nilai kosong, dan rentang nilai.
- Menghitung rata-rata, median, jumlah nilai di bawah batas latihan, dan korelasi sederhana.
- Menampilkan laporan di terminal.
- Menyimpan dua grafik PNG ke folder `outputs/`.
- Menyediakan pengujian dasar menggunakan `unittest`.

## Struktur proyek
```text
student-performance-analyzer/
├── data/student_performance.csv
├── src/main.py
├── tests/test_main.py
├── outputs/
├── requirements.txt
└── README.md
```

## Persyaratan
- Python 3.10 atau lebih baru disarankan.
- pip.
- Git hanya diperlukan untuk mengunggah proyek ke GitHub.

## Cara menjalankan di Windows (PowerShell)
1. Buka folder proyek di VS Code.
2. Buat virtual environment:
   ```powershell
   py -m venv .venv
   ```
3. Aktifkan:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
   Jika PowerShell memblokir aktivasi, gunakan Command Prompt dan jalankan:
   ```bat
   .venv\Scripts\activate.bat
   ```
4. Pasang dependensi:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Jalankan program:
   ```powershell
   python src/main.py
   ```
6. Periksa grafik yang dibuat di folder `outputs/`.

## Menjalankan pengujian
Dari folder utama proyek:
```powershell
python -m unittest discover -s tests -v
```

## Hubungan dengan CRISP-DM
1. **Business Understanding:** memahami pola nilai dan menyiapkan pertanyaan analisis.
2. **Data Understanding:** memahami kolom waktu belajar, kehadiran, dan nilai.
3. **Data Preparation:** memeriksa kolom, mengonversi angka, dan menangani baris yang tidak lengkap.
4. **Modelling:** proyek dasar ini tidak melatih model prediksi; korelasi hanya digunakan untuk eksplorasi.
5. **Evaluation:** memeriksa kewajaran hasil dan menjalankan pengujian.
6. **Deployment:** menjalankan program dari terminal dan menyimpan grafik sebagai keluaran.

## Empat level analitik
- **Descriptive:** ringkasan statistik dan distribusi nilai.
- **Diagnostic:** eksplorasi pola antara waktu belajar, kehadiran, dan nilai. Ini tidak membuktikan sebab-akibat.
- **Predictive:** belum diterapkan pada versi dasar.
- **Prescriptive:** rekomendasi awal berbasis aturan untuk meninjau kelompok yang perlu dukungan; bukan keputusan otomatis.

## Batasan dan etika
- Dataset ini dibuat untuk latihan, bukan data mahasiswa nyata.
- Batas nilai 60 adalah asumsi untuk demonstrasi, bukan standar kelulusan resmi.
- Korelasi tidak membuktikan sebab-akibat.
- Jangan menggunakan program ini untuk mengambil keputusan akademik nyata tanpa data yang sah, konteks yang memadai, evaluasi, dan peninjauan manusia.

## CRISP-DM bersifat iteratif
Jika hasil tidak menjawab pertanyaan awal, revisi pertanyaan, kualitas data, atau analisis. Tahapan tidak selalu berlangsung satu arah.

## Lisensi
Pilih lisensi sebelum membagikan proyek secara publik, jika diperlukan untuk tugas.
