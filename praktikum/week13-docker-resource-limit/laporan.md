
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

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
1. [Mengapa container perlu dibatasi CPU dan memori?]  
   **Karena container berbagi resource host.
Kalau tidak dibatasi:
Satu container bisa menghabiskan CPU/memori berlebihan, Container lain jadi lambat atau crash, Server jadi tidak stabil**  
2. [Apa perbedaan VM dan container dalam konteks isolasi resource?]  
   **VM lebih aman tapi berat, container lebih efisien tapi perlu pengaturan limit.**  
3. [Apa dampak limit memori terhadap aplikasi yang boros memori?]  
   **Kalau aplikasi pakai memori melebihi limit: Container bisa dimatikan otomatis (OOM Kill), Aplikasi crash atau restart, Performa jadi tidak stabil
Artinya:
Limit memori itu pengaman, tapi kalau terlalu kecil → aplikasi gagal jalan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
