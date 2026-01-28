# Simulasi Page Replacement FIFO dan LRU

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
