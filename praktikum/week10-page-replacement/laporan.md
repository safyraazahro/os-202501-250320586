
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Safyra Azahro  
- **NIM**   : 250320586  
- **Kelas** : 1 DSRA

---

## Tujuan
Praktikum ini bertujuan untuk memahami mekanisme page replacement pada sistem operasi serta membandingkan performa algoritma FIFO dan LRU berdasarkan jumlah page fault.

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
from collections import deque

def fifo_page_replacement(reference_string, frames):
    memory = deque()
    page_faults = 0

    print("=== FIFO Page Replacement ===")
    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) == frames:
                memory.popleft()
            memory.append(page)
            status = "FAULT"
        else:
            status = "HIT"
        print(f"Page: {page} | Memory: {list(memory)} | {status}")

    print(f"Total Page Fault (FIFO): {page_faults}\n")
    return page_faults


def lru_page_replacement(reference_string, frames):
    memory = []
    page_faults = 0

    print("=== LRU Page Replacement ===")
    for page in reference_string:
        if page not in memory:
            page_faults += 1
            if len(memory) == frames:
                memory.pop(0)
            memory.append(page)
            status = "FAULT"
        else:
            memory.remove(page)
            memory.append(page)
            status = "HIT"
        print(f"Page: {page} | Memory: {memory} | {status}")

    print(f"Total Page Fault (LRU): {page_faults}\n")
    return page_faults


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    fifo_faults = fifo_page_replacement(reference_string, frames)
    lru_faults = lru_page_replacement(reference_string, frames)

    print("=== Perbandingan ===")
    print(f"FIFO Page Faults: {fifo_faults}")
    print(f"LRU Page Faults : {lru_faults}")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
| Algoritma | Jumlah Page Fault | Keterangan      |
|---------- |------------------|------------------|
| FIFO      | 10 | Berdasarkan urutan masuk       |
| LRU       | 9 | Berdasarkan penggunaan terakhir | 

Algoritma LRU menghasilkan page fault lebih sedikit dibanding FIFO.
Hal ini karena LRU mempertimbangkan pola penggunaan halaman sebelumnya,
sementara FIFO tidak memperhatikan frekuensi atau waktu akses halaman.

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
