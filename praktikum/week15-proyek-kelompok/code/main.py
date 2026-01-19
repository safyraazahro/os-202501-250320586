import csv
from modules import scheduling, pagerepl
from utils.table import print_table

def load_processes():
    with open("data/process.csv") as f:
        return [
            {"pid": r["pid"], "arrival": int(r["arrival"]), "burst": int(r["burst"])}
            for r in csv.DictReader(f)
        ]

def scheduling_menu():
    procs = load_processes()
    algo = input("Pilih algoritma (FCFS/SJF): ").lower()

    if algo == "fcfs":
        res, gantt, aw, at, tp = scheduling.simulate_fcfs(procs)
    else:
        res, gantt, aw, at, tp = scheduling.simulate_sjf(procs)

    rows = [[p["pid"], p["arrival"], p["burst"], p["waiting"], p["turnaround"]] for p in res]
    print_table(["PID", "Arrival", "Burst", "Waiting", "Turnaround"], rows)

    print("\n Statistik:")
    print("Average Waiting Time :", round(aw, 2))
    print("Average Turnaround  :", round(at, 2))
    print("Throughput          :", round(tp, 3))

    print("\n Gantt Chart:")
    for g in gantt:
        print(f"| {g[0]} ({g[1]}-{g[2]}) ", end="")
    print("|")


def pagerepl_menu():
    pages = list(map(int, open("data/pages.txt").read().split()))
    frames = int(input("Jumlah frame: "))
    algo = input("Pilih FIFO/LRU: ").lower()

    if algo == "fifo":
        faults, hit_ratio, history = pagerepl.fifo(pages, frames)
    else:
        faults, hit_ratio, history = pagerepl.lru(pages, frames)

    rows = [[p, f, s] for p, f, s in history]
    print_table(["Page", "Frame", "Status"], rows)

    print("\nPage Faults:", faults)
    print("Hit Ratio  :", round(hit_ratio, 2))


def main():
    while True:
        print("\n=== Mini OS Simulator ===")
        print("1. CPU Scheduling")
        print("2. Page Replacement")
        print("0. Exit")

        choice = input("Pilih menu: ")
        if choice == "1":
            scheduling_menu()
        elif choice == "2":
            pagerepl_menu()
        elif choice == "0":
            break
        else:
            print("Input tidak valid.")

if __name__ == "__main__":
    main()
