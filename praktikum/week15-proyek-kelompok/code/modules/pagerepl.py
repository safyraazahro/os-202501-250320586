def fifo(pages, frames):
    frame = []
    history = []
    faults = 0

    for p in pages:
        hit = p in frame
        if not hit:
            faults += 1
            if len(frame) < frames:
                frame.append(p)
            else:
                frame.pop(0)
                frame.append(p)

        history.append((p, list(frame), "HIT" if hit else "FAULT"))

    hit_ratio = (len(pages) - faults) / len(pages)
    return faults, hit_ratio, history


def lru(pages, frames):
    frame = []
    history = []
    faults = 0

    for p in pages:
        if p in frame:
            frame.remove(p)
            frame.append(p)
            status = "HIT"
        else:
            faults += 1
            status = "FAULT"
            if len(frame) < frames:
                frame.append(p)
            else:
                frame.pop(0)
                frame.append(p)

        history.append((p, list(frame), status))

    hit_ratio = (len(pages) - faults) / len(pages)
    return faults, hit_ratio, history