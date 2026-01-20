# Laporan Proyek Kelompok week 15 : Mini Simulasi Sistem Operasi (Scheduling + Memory + Container)

**Mata Kuliah:** Sistem Operasi

**Topik:** Integrasi CPU Scheduling, Page Replacement, dan Docker Containerization

---

## 1. Pendahuluan

### 1.1 Latar Belakang

Pemahaman mendalam mengenai mekanisme internal Sistem Operasi (SO) seperti penjadwalan proses dan manajemen memori seringkali sulit dicapai hanya melalui teori. Simulasi berbasis perangkat lunak menjadi sarana efektif untuk memvisualisasikan bagaimana algoritma OS bekerja dalam mengelola sumber daya terbatas secara efisien.

### 1.2 Tujuan

* Mengintegrasikan konsep **CPU Scheduling** dan **Page Replacement** ke dalam satu aplikasi terpadu.
* Mengimplementasikan workflow pengembangan perangkat lunak kolaboratif menggunakan Git.
* Memastikan portabilitas aplikasi menggunakan teknologi **Docker**.

---

## 2. Arsitektur Aplikasi

Aplikasi ini dirancang sebagai aplikasi berbasis terminal (CLI) dengan struktur modular. Setiap modul berfungsi secara independen namun terhubung melalui menu utama.

**Alur Kerja Aplikasi:**

1. **Input:** Pengguna memasukkan data melalui file CSV atau input manual.
2. **Processing:** Data dikirim ke engine simulasi (Scheduling/Memory).
3. **Output:** Hasil perhitungan ditampilkan dalam bentuk tabel metrik di terminal.

---

## 3. Pembagian Peran dan Kontribusi

Pengerjaan proyek ini dilakukan secara kolaboratif dengan pembagian peran sebagai berikut:

| No | Nama Anggota              | Peran                          | Kontribusi Utama                                                                                                                  |
|----|---------------------------|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| 1  | **Safyra Azahro**          | Project Lead / Integrator      | Mengkoordinasikan tim, melakukan merge pull request, serta memastikan integrasi modul dan Docker berjalan                        |
| 2  | **Aulia Zahra Fatmawati**  | Developer Modul A (Scheduling)| Mengimplementasikan modul CPU Scheduling (FCFS & SJF), menghitung waiting time dan turnaround time, serta menampilkan tabel hasil |
| 3  | **Ayu Ida Nuraini**        | Developer Modul B (Memory)    | Mengimplementasikan modul Page Replacement (FIFO & LRU), menghitung page fault dan hit ratio, serta menyiapkan input dataset      |
| 4  | **Aisyah Nurur Rohmah**    | Dokumentasi & Visualisasi     | Menyiapkan screenshot hasil running aplikasi                                                                                      |
| 5  | **Faizatun Khasanah**      | Dokumentasi Laporan           | Menyusun dan merapikan `laporan.md` dan `README.md`, serta penulisan analisis singkat                                             |

---

## 4. Hasil Pengujian dan Analisis

### 4.1 Modul A – CPU Scheduling

Berdasarkan pengujian dengan algoritma **SJF (Shortest Job First)**:

* **Total Proses:** 5
* **Avg Waiting Time:** [Hasil] ms
* **Avg Turnaround Time:** [Hasil] ms

### 4.2 Modul B – Page Replacement

Berdasarkan pengujian dengan algoritma **LRU (Least Recently Used)**:

* **Jumlah Frame:** 3
* **Total Page Faults:** [Hasil]
* **Hit Ratio:** [Hasil]%

---

## 5. Jawaban Quiz

**1. Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?**
Tantangan terbesar adalah menyeragamkan struktur data input. Modul Scheduling membutuhkan atribut waktu (arrival/burst), sedangkan Page Replacement membutuhkan deret referensi angka.

* **Solusi:** Kami membuat modul *Data Parser* terpusat yang mampu memilah kolom CSV yang relevan untuk setiap modul secara otomatis.

**2. Mengapa Docker membantu proses demo dan penilaian proyek?**
Docker mengisolasi dependensi aplikasi (seperti versi bahasa pemrograman atau library tertentu). Dengan Docker, tim penilai tidak perlu menginstal environment di komputer mereka; cukup menjalankan perintah `docker run`, aplikasi dipastikan berjalan persis seperti di komputer pengembang.

**3. Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.**
Modul **Page Replacement (terutama LRU)** akan paling terdampak. Hal ini karena setiap kali ada referensi halaman baru, algoritma harus melakukan pencarian dan pembaruan posisi pada struktur data (stack/list) untuk menentukan halaman mana yang paling lama tidak digunakan. Operasi ini memiliki kompleksitas yang meningkat seiring panjangnya barisan referensi halaman.

---

## 6. Penutup

Proyek ini berhasil mendemonstrasikan bagaimana konsep abstrak sistem operasi dapat diwujudkan dalam kode program yang fungsional. Penggunaan Docker terbukti mempermudah distribusi aplikasi, sementara Git membantu tim bekerja secara paralel tanpa mengganggu kode satu sama lain.

---
