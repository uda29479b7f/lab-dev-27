# small utilities, no deps

def clamp(value, low, high):
    return max(low, min(value, high))

def load_lines(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

if __name__ == "__main__":
    print(list(chunks(range(16), 3)))

# quick sketch
