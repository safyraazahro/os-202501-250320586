
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Safyra azahro]  
- **NIM**   : [250320586]  
- **Kelas** : [1 IDSRA]

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


## Tugas
400-500 kata 
Analisis: Pentingnya System Call untuk Keamanan OS dan Mekanisme Keamanan Transisi User–Kernel

1. Pentingnya System Call untuk Keamanan OS

System call adalah antarmuka utama antara program pengguna (user space) dan kernel dalam sistem operasi. Karena kernel memiliki hak istimewa tertinggi (privileged mode), sementara program pengguna berjalan dengan hak terbatas, semua akses ke sumber daya penting—seperti memori, berkas, perangkat keras, dan jaringan—harus melalui system call. Hal ini menjadikan system call sebagai gerbang utama keamanan (security gateway) bagi sistem operasi.

Tanpa mekanisme system call yang terkontrol, program pengguna dapat langsung mengakses memori kernel atau perangkat keras, yang berpotensi menimbulkan kebocoran data, korupsi memori, atau eskalasi hak akses. Oleh karena itu, system call tidak hanya berfungsi sebagai alat komunikasi, tetapi juga sebagai lapisan pertahanan. Kernel menggunakan validasi parameter, pemeriksaan izin (permission checking), dan pengelolaan konteks untuk memastikan bahwa setiap permintaan dari user space sah dan aman untuk dijalankan.

Sebagai contoh, saat aplikasi mencoba membuka file dengan system call open(), kernel memeriksa apakah proses tersebut memiliki izin membaca atau menulis pada file yang dimaksud. Jika tidak, kernel menolak permintaan tersebut dengan mengembalikan kode kesalahan seperti EACCES. Dengan cara ini, system call membantu mencegah penyalahgunaan sumber daya sistem oleh aplikasi berbahaya atau bug yang tidak disengaja.

2. Keamanan dalam Transisi User–Kernel

Transisi antara mode pengguna (user mode) dan mode kernel (kernel mode) merupakan titik kritis dalam keamanan sistem operasi. OS harus memastikan bahwa proses ini berlangsung aman, terisolasi, dan terkendali.

Transisi dimulai ketika aplikasi memanggil system call. Biasanya, ini dilakukan melalui instruksi khusus prosesor seperti syscall (pada arsitektur x86-64) atau int 0x80 (pada sistem lama). Instruksi ini memicu trap ke kernel, menyebabkan CPU beralih dari user mode ke kernel mode, dan menjalankan fungsi system call handler yang relevan.

Untuk menjaga keamanan, OS melakukan beberapa langkah:

Validasi argumen: Kernel memeriksa alamat memori yang diberikan oleh proses agar tidak mengarah ke wilayah memori kernel.

Isolasi konteks: Kernel memiliki ruang alamat memori sendiri yang tidak dapat diakses oleh program pengguna secara langsung.

Pemulihan konteks aman: Setelah eksekusi system call selesai, kontrol dikembalikan ke user space dengan status dan register CPU yang sudah diverifikasi.

Dengan pendekatan ini, sistem operasi mencegah user program melakukan eksekusi kode arbitrer di level kernel, yang dapat berakibat fatal bagi keamanan sistem.

3. Contoh System Call di Linux

Beberapa system call yang paling umum digunakan di Linux antara lain:

read() dan write() – untuk operasi input/output pada file atau perangkat.

open() dan close() – untuk membuka dan menutup file.

fork() – untuk membuat proses baru.

exec() – untuk mengeksekusi program lain.

wait() – untuk menunggu proses anak selesai.

socket(), bind(), connect() – untuk komunikasi jaringan.

mmap() – untuk memetakan file atau perangkat ke memori.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

System call adalah elemen vital yang menjaga keseimbangan antara fungsionalitas dan keamanan sistem operasi. Melalui validasi, isolasi, dan kontrol ketat pada transisi user–kernel, OS memastikan bahwa hanya permintaan sah yang dapat dijalankan, sehingga melindungi integritas dan stabilitas sistem secara keseluruhan.

---

## Quiz
1. [Pertanyaan 1]  
   **Fungsi utama system call adalah sebagai antarmuka (interface) agar program dapat meminta layanan dari kernel (inti) sistem operasi, seperti manajemen proses, manajemen file, manajemen perangkat, dan komunikasi. Ini memungkinkan aplikasi untuk mengakses sumber daya sistem secara aman dan terkontrol.**

2. [Pertanyaan 2]  
   **Empat kategori system call yang umum digunakan adalah:
•Kontrol Proses: Meliputi pembuatan, eksekusi, dan penghentian proses. 
•Manajemen Berkas (File Management): Meliputi operasi pada berkas seperti membuat, membaca, menulis, dan menghapus. 
•Manajemen Perangkat (Device Management): Meliputi permintaan dan pelepasan perangkat, serta membaca dan menulis dari perangkat. 
•Komunikasi: Meliputi pertukaran informasi antarproses atau antar komputer.**  

3. [Pertanyaan 3]  
   **Panggilan sistem (system call) tidak bisa dipanggil langsung oleh program pengguna karena alasan keamanan dan stabilitas sistem operasi.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
