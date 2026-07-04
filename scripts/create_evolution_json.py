import json

commits = [
    "81ad9fae",
    "e1efeeb6",
    "2197cd47",
    "17c3dcee",
    "1c2bc7f6",
    "d5bd5331",
    "ec08e647",
    "d34664b0"
]

data = []

for commit in commits:

    file = f"{commit}_graph.json"

    with open(file) as f:
        graph = json.load(f)

    data.append({
        "commit": commit,
        "nodes": len(graph["nodes"]),
        "edges": len(graph["links"])
    })

with open("evolution.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved evolution.json")
