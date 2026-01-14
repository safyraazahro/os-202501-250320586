
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Safyra Azahro  
- **NIM**   : 250320586  
- **Kelas** : 1 DSRA

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
1. **FIFO (First In, First Out) dan LRU (Least Recently Used) adalah algoritma penggantian halaman dalam sistem operasi, digunakan untuk mengelola memori virtual saat terjadi page fault (ketika halaman yang dibutuhkan tidak ada di memori utama). Kedua algoritma ini bertujuan meminimalkan page fault, tetapi cara kerjanya berbeda.**  
2. **FIFO dapat menghasilkan Belady’s Anomaly karena keputusan penggantian halaman hanya berdasarkan urutan kedatangan, bukan pola penggunaan, sehingga tidak menjamin bahwa penambahan frame akan mengurangi page fault.**  
3. **LRU (Least Recently Used) umumnya menghasilkan performa lebih baik dibanding FIFO karena LRU selaras dengan prinsip locality of reference, sedangkan FIFO tidak.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
