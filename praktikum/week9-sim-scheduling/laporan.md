
# Laporan Praktikum Minggu 9
Topik: Sim Scheduling

---

## Identitas
- **Nama**  : [Safyra Azahro]  
- **NIM**   : [250320586]  
- **Kelas** : [1 DSRA]

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

# ==============================
# Simulasi Algoritma FCFS
# Tanpa Completion Time
# ==============================

# Dataset proses (database)
processes = [
    {"process": "P1", "arrival": 0, "burst": 6},
    {"process": "P2", "arrival": 1, "burst": 8},
    {"process": "P3", "arrival": 2, "burst": 7},
    {"process": "P4", "arrival": 3, "burst": 3},
]

# Urutkan berdasarkan Arrival Time (FCFS)
processes.sort(key=lambda x: x["arrival"])

current_time = 0
total_wt = 0
total_tat = 0

print("=== SIMULASI CPU SCHEDULING FCFS ===")
print("-" * 60)
print(f"{'Process':<10}{'Arrival':<10}{'Burst':<10}"
      f"{'Turnaround':<15}{'Waiting':<10}")
print("-" * 60)

for p in processes:
    if current_time < p["arrival"]:
        current_time = p["arrival"]

    # Hitung Turnaround & Waiting Time
    turnaround_time = (current_time + p["burst"]) - p["arrival"]
    waiting_time = turnaround_time - p["burst"]

    total_wt += waiting_time
    total_tat += turnaround_time

    print(f"{p['process']:<10}{p['arrival']:<10}{p['burst']:<10}"
          f"{turnaround_time:<15}{waiting_time:<10}")

    current_time += p["burst"]

n = len(processes)

print("-" * 60)
print(f"Average Waiting Time    : {total_wt / n:.2f}")
print(f"Average Turnaround Time : {total_tat / n:.2f}")

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
1. **Simulasi diperlukan untuk menguji algoritma scheduling karena memungkinkan pengujian tanpa risiko pada sistem nyata, mudah mengatur berbagai skenario beban kerja, membandingkan kinerja algoritma secara adil, serta menghemat waktu dan biaya sebelum algoritma diterapkan secara langsung.**  
2. **Simulasi: cepat, akurat, dan mampu menangani banyak data. Perhitungan manual: lambat, rawan kesalahan, dan tidak praktis. Kesimpulan: simulasi lebih efisien dan andal daripada perhitungan manual.**  
3.  **Algoritma FCFS (First Come First Served) paling mudah diimplementasikan karena proses dijalankan sesuai urutan kedatangan tanpa perhitungan kompleks, prioritas, atau preemption. Struktur dan logikanya sederhana sehingga mudah dipahami dan diterapkan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
