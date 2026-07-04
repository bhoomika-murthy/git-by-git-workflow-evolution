import json

with open("old_graph.json") as f:
    old = json.load(f)

with open("new_graph.json") as f:
    new = json.load(f)

old_nodes = {n["id"] for n in old["nodes"]}
new_nodes = {n["id"] for n in new["nodes"]}

old_edges = {(e["source"], e["target"]) for e in old["links"]}
new_edges = {(e["source"], e["target"]) for e in new["links"]}

added_nodes = sorted(new_nodes - old_nodes)
removed_nodes = sorted(old_nodes - new_nodes)

added_edges = sorted(new_edges - old_edges)
removed_edges = sorted(old_edges - new_edges)

print("=== NODES ===")
print(f"Added nodes: {len(added_nodes)}")
print(f"Removed nodes: {len(removed_nodes)}")

print("\n=== EDGES ===")
print(f"Added edges: {len(added_edges)}")
print(f"Removed edges: {len(removed_edges)}")

print("\n--- Added Nodes ---")
for n in added_nodes:
    print(n)

print("\n--- Removed Nodes ---")
for n in removed_nodes:
    print(n)

print("\n--- Added Edges ---")
for s, t in added_edges:
    print(f"{s} -> {t}")

print("\n--- Removed Edges ---")
for s, t in removed_edges:
    print(f"{s} -> {t}")
