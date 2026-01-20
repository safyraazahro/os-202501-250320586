def simulate_fcfs(processes):
    time = 0
    gantt = []
    result = []

    for p in processes:
        start = max(time, p["arrival"])
        wait = start - p["arrival"]
        finish = start + p["burst"]
        tat = finish - p["arrival"]

        gantt.append((p["pid"], start, finish))
        time = finish

        result.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": wait,
            "turnaround": tat
        })

    avg_wait = sum(p["waiting"] for p in result) / len(result)
    avg_tat = sum(p["turnaround"] for p in result) / len(result)
    throughput = len(result) / time

    return result, gantt, avg_wait, avg_tat, throughput


def simulate_sjf(processes):
    time = 0
    ready = processes.copy()
    done = []
    gantt = []

    while ready:
        available = [p for p in ready if p["arrival"] <= time]
        if not available:
            time += 1
            continue

        p = min(available, key=lambda x: x["burst"])
        ready.remove(p)

        start = time
        finish = start + p["burst"]
        wait = start - p["arrival"]
        tat = finish - p["arrival"]

        gantt.append((p["pid"], start, finish))
        time = finish

        done.append({
            "pid": p["pid"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "waiting": wait,
            "turnaround": tat
        })

    avg_wait = sum(p["waiting"] for p in done) / len(done)
    avg_tat = sum(p["turnaround"] for p in done) / len(done)
    throughput = len(done) / time

    return done, gantt, avg_wait, avg_tat, throughput