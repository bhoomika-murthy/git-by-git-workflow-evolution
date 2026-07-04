import json
import glob

files = sorted(
    f for f in glob.glob("*_graph.json")
    if f != "dag_graph.json"
)
changes = []

for i in range(1, len(files)):

    prev = files[i-1]
    curr = files[i]

    with open(prev) as f:
        g1 = json.load(f)

    with open(curr) as f:
        g2 = json.load(f)

    n1 = {x["id"] for x in g1["nodes"]}
    n2 = {x["id"] for x in g2["nodes"]}

    added = sorted(list(n2 - n1))
    removed = sorted(list(n1 - n2))

    changes.append({
        "from": prev,
        "to": curr,
        "added": added,
        "removed": removed
    })

with open("changes.json", "w") as f:
    json.dump(changes, f, indent=2)

print("Saved changes.json")
