
# Laporan Praktikum Minggu 11
Topik:  Simulasi dan Deteksi Deadlock

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
 import csv

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            p = row['Process']
            a = row['Allocation']
            r = row['Request']

            processes.append(p)
            allocation[p] = a
            request[p] = r

    return processes, allocation, request

def detect_deadlock(processes, allocation, request):
    # Build wait-for graph
    wait_for = {p: None for p in processes}

    for p in processes:
        for q in processes:
            if request[p] == allocation[q]:
                wait_for[p] = q

    # Detect cycle
    visited = set()
    deadlock_processes = set()

    for p in processes:
        slow = p
        fast = p

        while fast in wait_for and wait_for[fast]:
            slow = wait_for.get(slow)
            fast = wait_for.get(wait_for.get(fast))

            if slow is None or fast is None:
                break

            if slow == fast:
                # Cycle detected
                curr = slow
                while curr not in deadlock_processes:
                    deadlock_processes.add(curr)
                    curr = wait_for[curr]
                break

    return deadlock_processes

if __name__ == "__main__":
    processes, allocation, request = read_dataset("dataset_deadlock.csv")
    deadlock = detect_deadlock(processes, allocation, request)

    print("=== HASIL DETEKSI DEADLOCK ===")
    if deadlock:
        print("Deadlock terdeteksi pada proses:")
        for p in deadlock:
            print("-", p)
    else:
        print("Tidak terjadi deadlock.")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## AnalisiS
Tabel Hasil Deteksi
Proses	Status
P1	Deadlock
P2	Deadlock
P3	Deadlock
Interpretasi

Deadlock terjadi karena:
Mutual Exclusion – Resource hanya bisa dipakai satu proses.
Hold and Wait – Proses memegang resource sambil menunggu resource lain.
No Preemption – Resource tidak bisa diambil paksa.
Circular Wait – P1 → P2 → P3 → P1.

Semua empat kondisi deadlock terpenuhi, sehingga sistem berada dalam kondisi deadlock.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?  
   **1. Perbedaan deadlock prevention, avoidance, dan detection, -Prevention: Mencegah salah satu kondisi deadlock terjadi, -Avoidance: Menghindari deadlock dengan analisis kondisi aman- Detection: Mengizinkan deadlock terjadi lalu mendeteksinya** 
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi? 
   **Karena pencegahan dan penghindaran deadlock dapat menurunkan efisiensi sistem.**  
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock? 
   **-Kelebihan: Lebih fleksibel dan efisien, -Kekurangan: Deadlock sudah terlanjur terjadi dan perlu recovery**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
