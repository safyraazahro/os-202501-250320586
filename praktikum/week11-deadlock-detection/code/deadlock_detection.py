import csv

def read_dataset(filename):
    processes = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes[row['Process']] = {
                'allocation': row['Allocation'],
                'request': row['Request']
            }
    return processes


def detect_deadlock(processes):
    graph = {}

    # Bangun graph: P -> R -> P
    for p in processes:
        graph[p] = processes[p]['request']

    visited = set()

    def has_cycle(start):
        current = start
        path = set()

        while current not in path:
            path.add(current)
            resource = graph[current]

            # Cari proses yang memegang resource tersebut
            next_process = None
            for p in processes:
                if processes[p]['allocation'] == resource:
                    next_process = p
                    break

            if next_process is None:
                return False

            current = next_process

        return True

    deadlocked = []
    for p in processes:
        if has_cycle(p):
            deadlocked.append(p)

    return set(deadlocked)


if __name__ == "__main__":
    dataset = read_dataset("dataset_deadlock.csv")
    deadlock_processes = detect_deadlock(dataset)

    print("=== Deadlock Detection Result ===")
    if deadlock_processes:
        print("Deadlock detected!")
        print("Processes involved:")
        for p in deadlock_processes:
            print("-", p)
    else:
        print("No deadlock detected.")
