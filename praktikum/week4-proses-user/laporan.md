
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Safyra Azahro]  
- **NIM**   : [250320586]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Sebagai sistem pertama yang berjalan setelah kernel Linux di-boot, yang bertugas memulai, mengelola, dan menghentikan semua proses dan layanan lainnya yang diperlukan agar sistem operasi berfungsi dan berjalan. systemd sendiri adalah sistem init modern yang menggantikan sistem init lama (seperti SysVinit), menawarkan lebih banyak fleksibilitas, efisiensi, dan fitur manajemen layanan yang canggih.**
   
3. [Pertanyaan 2]  
   **Perbedaan utama adalah kill menghentikan satu proses berdasarkan ID Proses (PID), sedangkan killall menghentikan semua proses yang cocok berdasarkan nama prosesnya. kill menawarkan presisi lebih tinggi untuk menargetkan satu proses, sementara killall lebih fleksibel untuk mematikan semua instance dari program tertentu secara sekaligus.**
   
5. [Pertanyaan 3]  
   **User root memiliki hak istimewa di sistem Linux karena ia adalah akun administrator dengan akses tanpa batas ke semua file dan fungsi sistem, yang diperlukan untuk tugas-tugas seperti menginstal perangkat lunak, mengelola pengguna, dan mengubah konfigurasi sistem. Meskipun diperlukan untuk kelancaran operasi, hak ini membuat root sangat berbahaya jika disalahgunakan, sehingga praktik terbaik adalah membatasi penggunaan akses root secara langsung dan menggunakannya hanya saat benar-benar diperlukan melalui perintah sudo.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
