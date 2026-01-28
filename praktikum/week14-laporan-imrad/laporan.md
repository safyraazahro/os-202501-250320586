
# Laporan Praktikum Minggu 14
Topik: Penyusunan Laporan Praktikum Format IMRAD

---

## Identitas
- **Nama**  : Safyra Azahro  
- **NIM**   : 250320586
- **Kelas** : 1 DSRA

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Contoh:  
> Menyusun laporan praktikum dengan struktur ilmiah (Pendahuluan–Metode–Hasil–Pembahasan–Kesimpulan).
Menyajikan hasil uji dalam bentuk tabel dan/atau grafik yang jelas.
Menuliskan analisis hasil dengan argumentasi yang logis.
Menyusun sitasi dan daftar pustaka dengan format yang konsisten.
Mengunggah draft laporan ke repositori dengan rapi dan tepat waktu.

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

## Pendahuluan (Introduction)

**Latar Belakang**
Pengelolaan memori merupakan bagian penting dalam sistem operasi karena berperan dalam mengatur penggunaan memori agar berjalan secara efisien. Salah satu permasalahan yang sering muncul adalah kondisi ketika memori utama penuh, sehingga sistem harus menentukan halaman (page) mana yang perlu diganti. Proses ini dikenal sebagai page replacement.
FIFO (First-In First-Out) dan LRU (Least Recently Used) adalah dua algoritma page replacement yang umum digunakan. Algoritma FIFO mengganti halaman yang pertama kali masuk ke memori, sedangkan LRU mengganti halaman yang paling lama tidak digunakan. Perbedaan cara kerja tersebut dapat memengaruhi jumlah page fault yang terjadi selama proses berjalan.
Oleh karena itu, praktikum ini dilakukan untuk membandingkan kinerja algoritma FIFO dan LRU berdasarkan jumlah page fault yang dihasilkan melalui simulasi.

**Rumusan Masalah**
1. Bagaimana perbandingan jumlah page fault antara algoritma FIFO dan LRU?
2. Algoritma mana yang lebih efektif dalam mengelola memori berdasarkan hasil simulasi?

**Tujuan Praktikum**
1. Memahami cara kerja algoritma FIFO dan LRU pada proses page replacement.
2. Membandingkan jumlah page fault yang dihasilkan oleh algoritma FIFO dan LRU.
3. Menentukan algoritma page replacement yang lebih efektif berdasarkan hasil pengujian.

## Metode (Methods)

**Lingkungan Uji**
- Sistem Operasi: Windows 10 / Windows 11
- Editor/Kode: Visual Studio Code, cmd
- Bahasa/Alat: Python (simulasi)
- Media eksekusi: Terminal Visual Studio Code, cmd
- Jumlah frame memori: 3 dan 4 frame

**Langkah Eksperimen**
1. Menentukan urutan referensi halaman.
2. Menjalankan simulasi FIFO dan LRU dengan jumlah frame tertentu.
3. Mencatat jumlah page fault yang terjadi.

**Parameter Uji**
-Urutan referensi: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
-Frame: 3 dan 4

## Hasil (Results)
Tabel berikut menunjukkan jumlah page fault yang dihasilkan oleh masing-masing algoritma.

*TabeL Perbandingan Jumlah Page Fault*
| Algoritma | 3 Frame | 4 Frame |
|----------|---------|---------|
| FIFO     | 9       | 10      |
| LRU      | 8       | 7       |


## Pembahasan (Discussion)
Hasil praktikum menunjukkan adanya perbedaan kinerja yang cukup jelas antara algoritma FIFO dan LRU. Pada pengujian dengan 3 frame, algoritma LRU menghasilkan jumlah page fault yang lebih sedikit dibandingkan FIFO. Hal ini terjadi karena LRU mengganti halaman yang paling lama tidak digunakan, sehingga halaman yang sering diakses tetap berada di memori.

Sebaliknya, algoritma FIFO tidak memperhatikan pola penggunaan halaman. FIFO hanya mengganti halaman yang pertama kali masuk ke memori, meskipun halaman tersebut masih sering digunakan. Akibatnya, pada beberapa kondisi FIFO menghasilkan page fault yang lebih banyak. Bahkan pada pengujian dengan 4 frame, jumlah page fault FIFO justru meningkat. Kondisi ini dikenal sebagai Belady’s Anomaly, yaitu keadaan di mana penambahan jumlah frame tidak selalu meningkatkan kinerja sistem.

Hasil yang diperoleh sudah sesuai dengan teori yang dijelaskan pada materi perkuliahan, di mana LRU umumnya lebih efisien dibandingkan FIFO karena memanfaatkan prinsip locality of reference. Namun, praktikum ini masih memiliki keterbatasan, seperti jumlah data uji yang relatif sedikit dan simulasi yang belum memperhitungkan kompleksitas implementasi algoritma di sistem operasi nyata.

** Kesimpulan**
1. Algoritma LRU secara umum lebih efisien dibandingkan FIFO dalam menekan jumlah page fault.
2. FIFO dapat mengalami Belady's anomaly pada kondisi tertentu.
3. Pemilihan algoritma page replacement berpengaruh signifikan terhadap kinerja manajemen memori.

## Daftar Pustaka
[1]**A. Silberschatz, P. B. Galvin, and G. Gagne, Operating System Concepts, 9th ed., Wiley, 2018.*

[2]**A. S. Tanenbaum and H. Bos, Modern Operating Systems, 4th ed., Pearson, 2015.*


---
## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```# Simulasi Page Replacement FIFO dan LRU

def fifo(pages, frames):
    memory = []
    page_fault = 0

    for page in pages:
        if page not in memory:
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
    return page_fault


def lru(pages, frames):
    memory = []
    page_fault = 0

    for page in pages:
        if page not in memory:
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
        else:
            memory.remove(page)
            memory.append(page)
    return page_fault


# Parameter uji
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_3 = 3
frame_4 = 4

# Output hasil
print("Hasil Simulasi Page Replacement")
print("Urutan Halaman:", pages)
print()

print("FIFO (3 frame):", fifo(pages, frame_3))
print("FIFO (4 frame):", fifo(pages, frame_4))
print("LRU  (3 frame):", lru(pages, frame_3))
print("LRU  (4 frame):", lru(pages, frame_4))
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## 

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?]  
   **Karena format IMRAD (Introduction, Methods, Results, and Discussion) menyusun laporan secara sistematis dan logis. Setiap bagian punya fungsi jelas, sehingga pembaca (terutama dosen) mudah memahami tujuan praktikum, cara kerja, hasil yang diperoleh, dan maknanya. Ini juga memudahkan evaluasi karena penilaian bisa dilakukan per bagian.**  
2. [Apa perbedaan antara bagian Hasil dan Pembahasan?]  
   **Hasil: Menyajikan data atau temuan praktikum apa adanya (tabel, grafik, angka) tanpa opini atau penafsiran.
Pembahasan: Menjelaskan dan menafsirkan hasil tersebut, membandingkan dengan teori, serta menguraikan alasan mengapa hasilnya bisa seperti itu.**  
3. [Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?]  
   **Karena sitasi menunjukkan bahwa laporan didasarkan pada sumber ilmiah yang jelas dan terpercaya, bukan pendapat pribadi. Selain itu, sitasi mencegah plagiarisme, memperkuat keilmiahan laporan, dan memudahkan pembaca menelusuri sumber teori yang digunakan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
