
# Laporan Praktikum Minggu 1
Topik: Intro Arsitektur Os

---

## Identitas
- **Nama**  : [Safyra Azahro]  
- **NIM**   : [250320586]  
- **Kelas** : [1DSRA]

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
## Tugas
-Mengenal arsitektur sistem operasi — memahami perbedaan antara arsitektur monolithic kernel, microkernel.
-Melatih penggunaan perintah dasar OS (misalnya Linux/Unix) untuk memahami struktur file system dan kontrol proses.

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

## Tugas
1. Hasil percobaan menunjukkan bahwa interaksi antara program dan perangkat keras selalu melalui kernel menggunakan system call, sesuai teori arsitektur OS berlapis. Kernel bertindak sebagai perantara yang mengatur akses sumber daya dan keamanan sistem.

Efisiensi dan waktu eksekusi proses dipengaruhi oleh cara kernel mengelola context switching dan interrupt handling, sesuai dengan fungsi utama kernel dalam teori sistem operasi.

2. Perbedaan hasil di lingkungan OS berbeda (Linux vs Windows):

Pada Linux, akses dan pemanggilan system call lebih transparan dan efisien karena arsitekturnya lebih terbuka dan modular, sedangkan pada Windows, banyak fungsi kernel dibungkus dalam API tingkat tinggi sehingga performa dan hasil pengamatan bisa tampak berbeda.

Perbedaan arsitektur kernel (Linux monolitik vs Windows hibrida) menyebabkan variasi dalam penanganan proses, manajemen memori, dan performa I/O, yang dapat terlihat dari hasil pengujian waktu eksekusi atau perilaku proses di kedua sistem.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.


## Tugas
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

Hybrid kernel (contoh: Windows NT, macOS X dengan XNU kernel) mencoba menggabungkan kecepatan monolithic dengan keamanan dan modularitas microkernel. Model ini dianggap paling praktis untuk sistem operasi desktop dan server modern


Kesimpulan:
Model yang paling relevan saat ini adalah hybrid kernel, karena menawarkan keseimbangan antara performa, stabilitas, keamanan, dan modularitas. Namun, microkernel juga semakin relevan untuk konteks khusus seperti IoT, sistem real-time, dan sistem dengan kebutuhan keamanan tinggi. Sementara itu, monolithic kernel tetap kuat di komunitas open-source, terutama karena kecepatan dan ekosistemnya

---

## Quiz
 
## Tugas
1. Tiga fungsi utama sistem operasi:

-Manajemen sumber daya (Resource Management):
Mengatur penggunaan CPU, memori, perangkat input/output, dan penyimpanan agar berjalan efisien dan adil di antara proses yang aktif.

-Manajemen proses (Process Management):
Mengatur pembuatan, penjadwalan, dan penghentian proses serta komunikasi antarproses.

-Manajemen file (File Management):
Menyediakan sistem untuk penyimpanan, pengambilan, penamaan, dan pengaturan hak akses terhadap file di media penyimpanan.

2. Perbedaan antara Kernel Mode dan User Mode:
-Kernel
Memiliki akses penuh ke seluruh sumber daya sistem (memori, perangkat keras, dll.)
Digunakan oleh bagian inti OS (kernel) untuk menjalankan instruksi penting.
Kesalahan dapat menyebabkan sistem crash.
Manajemen memori, interrupt handling, device driver.

-User Mode
Terbatas, tidak dapat langsung mengakses perangkat keras atau area memori tertentu.
Digunakan oleh aplikasi pengguna agar sistem tetap aman dan stabil.
Kesalahan biasanya hanya memengaruhi aplikasi yang sedang berjalan.
Menjalankan program seperti browser, editor teks, dsb.

3. Contoh OS dengan arsitektur:

Monolithic Kernel:

Contoh: Linux, MS-DOS, Unix tradisional (System V, BSD)

Ciri: Semua layanan sistem (file system, device driver, dll.) berjalan dalam satu ruang kernel.

Microkernel:

Contoh: Minix, QNX, Mach (digunakan dalam macOS awal)

Ciri: Hanya fungsi dasar (seperti komunikasi antarproses dan manajemen memori) yang berada di kernel; layanan lain dijalankan di user space untuk stabilitas dan modularitas.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
