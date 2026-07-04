import json

graphs = [
    "81ad9fae_graph.json",
    "e1efeeb6_graph.json",
    "2197cd47_graph.json",
    "17c3dcee_graph.json",
    "1c2bc7f6_graph.json",
    "d5bd5331_graph.json",
    "ec08e647_graph.json",
    "d34664b0_graph.json"
]

for i in range(len(graphs)-1):

    g1 = graphs[i]
    g2 = graphs[i+1]

    with open(g1) as f:
        old = json.load(f)

    with open(g2) as f:
        new = json.load(f)

    old_nodes = {n["id"] for n in old["nodes"]}
    new_nodes = {n["id"] for n in new["nodes"]}

    old_edges = {(e["source"], e["target"]) for e in old["links"]}
    new_edges = {(e["source"], e["target"]) for e in new["links"]}

    print()
    print(f"{g1} -> {g2}")

    print(
        f"Added nodes: {len(new_nodes-old_nodes)}"
    )

    print(
        f"Removed nodes: {len(old_nodes-new_nodes)}"
    )

    print(
        f"Added edges: {len(new_edges-old_edges)}"
    )

    print(
        f"Removed edges: {len(old_edges-new_edges)}"
    )
