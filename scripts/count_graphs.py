import json
import glob

for file in sorted(glob.glob("*_graph.json")):
    with open(file) as f:
        data = json.load(f)

    print(
        file,
        "nodes =", len(data["nodes"]),
        "edges =", len(data["links"])
    )
