
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


Berikut ringkasan ±500 kata mengenai perbedaan monoliths kernel, microkernel, dan layered architecture, beserta contoh OS dan analisis relevansi untuk sistem modern:

Perbedaan Monolithic Kernel, Microkernel, dan Layered Architecture
1. Monolithic Kernel
Monolithic kernel adalah arsitektur sistem operasi di mana seluruh komponen inti sistem (manajemen proses, memori, file system, driver perangkat keras, dll) dijalankan dalam satu ruang kernel. Semua layanan sistem berjalan sebagai bagian dari kernel, sehingga interaksi antar komponen sangat cepat karena tidak memerlukan komunikasi antar proses (IPC).

Kelebihan:

Performa tinggi karena tidak ada overhead IPC.

Interaksi antar komponen cepat.

Kekurangan:

Sulit dipelihara karena semua modul saling tergantung.

Jika satu komponen gagal, bisa menyebabkan seluruh sistem crash.

Kurang aman karena semua komponen berjalan dengan hak akses penuh.

2. Microkernel
Microkernel hanya menyediakan layanan dasar kernel, seperti manajemen proses, memori, dan IPC. Fitur lain seperti device driver, file system, dan protokol jaringan berjalan di ruang pengguna sebagai server terpisah. Komunikasi antar modul dilakukan melalui IPC.

Kelebihan:

Lebih stabil dan aman karena sebagian besar layanan berjalan di ruang pengguna.

Jika satu layanan gagal, tidak serta-merta memengaruhi seluruh sistem.

Lebih modular, mudah dikembangkan atau diubah.

Kekurangan:

Kinerja lebih lambat dibanding monolith karena seringnya komunikasi antar proses (IPC).

Desain dan implementasi lebih kompleks.

3. Layered Architecture
Layered architecture membagi sistem operasi menjadi beberapa lapisan (layer), di mana setiap lapisan hanya berinteraksi dengan lapisan di bawahnya atau di atasnya. Misalnya, lapisan hardware di bawah, disusul oleh device drivers, manajemen memori, sistem file, hingga user interface.

Kelebihan:

Desain terstruktur, memudahkan pengembangan dan pemeliharaan.

Setiap lapisan bisa diuji secara terpisah.

Modularitas tinggi.

Kekurangan:

Bisa terjadi penurunan kinerja karena overhead dari komunikasi antar lapisan.

Kurang fleksibel jika ada kebutuhan untuk melewati lapisan (misalnya akses langsung hardware).

Contoh OS dengan Masing-Masing Model
Monolithic Kernel: Linux, Unix (FreeBSD), MS-DOS.

Microkernel: Minix, QNX, seL4, GNU Hurd, Mach (kernel awal Mac OS X).

Layered Architecture: THE OS (oleh Dijkstra), Multics (konsep awal), sebagian Windows NT (meskipun realisasinya tidak sepenuhnya berlapis).

Analisis: Model Mana yang Paling Relevan untuk Sistem Modern?
Untuk sistem modern, tidak ada satu model yang secara absolut paling unggul. Namun, tren saat ini menunjukkan kecenderungan ke arah modularitas dan keamanan, yang membuat microkernel dan hybrid kernel (gabungan monolithic dan microkernel) lebih relevan.

Monolithic kernel seperti Linux tetap populer karena performanya dan dukungan luas dari komunitas. Kernel ini terus berkembang ke arah modularitas (dengan loadable modules) untuk mengatasi kekurangan tradisional.

Microkernel banyak digunakan di sistem real-time, perangkat embedded, dan sistem yang membutuhkan keamanan tingkat tinggi (contoh: QNX di otomotif, seL4 di sistem militer). Namun, overhead komunikasi masih menjadi tantangan.

Hybrid kernel (contoh: Windows NT, macOS X dengan XNU kernel) mencoba menggabungkan kecepatan monolithic dengan keamanan dan modularitas microkernel. Model ini dianggap paling praktis untuk sistem operasi desktop dan server modern.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

Kesimpulan:
Model yang paling relevan saat ini adalah hybrid kernel, karena menawarkan keseimbangan antara performa, stabilitas, keamanan, dan modularitas. Namun, microkernel juga semakin relevan untuk konteks khusus seperti IoT, sistem real-time, dan sistem dengan kebutuhan keamanan tinggi. Sementara itu, monolithic kernel tetap kuat di komunitas open-source, terutama karena kecepatan dan ekosistemnya

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
