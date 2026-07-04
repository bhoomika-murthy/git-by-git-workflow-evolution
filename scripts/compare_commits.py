import json
import sys

old_file = sys.argv[1]
new_file = sys.argv[2]

with open(old_file) as f:
    old = json.load(f)

with open(new_file) as f:
    new = json.load(f)

old_nodes = {n["id"] for n in old["nodes"]}
new_nodes = {n["id"] for n in new["nodes"]}

old_edges = {(e["source"], e["target"]) for e in old["links"]}
new_edges = {(e["source"], e["target"]) for e in new["links"]}

print("===== SUMMARY =====")
print(f"Old nodes: {len(old_nodes)}")
print(f"New nodes: {len(new_nodes)}")
print(f"Old edges: {len(old_edges)}")
print(f"New edges: {len(new_edges)}")

print()
print(f"Added nodes: {len(new_nodes - old_nodes)}")
print(f"Removed nodes: {len(old_nodes - new_nodes)}")
print(f"Added edges: {len(new_edges - old_edges)}")
print(f"Removed edges: {len(old_edges - new_edges)}")
