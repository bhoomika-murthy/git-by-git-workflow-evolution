import json
import pydot

graph = pydot.graph_from_dot_file("dag.dot")[0]

nodes = set()

for node in graph.get_nodes():
    label = node.get_label()

    if label and "NFCORE_" in label:
        nodes.add(label.strip('"'))

json_nodes = [{"id": n} for n in sorted(nodes)]

with open("workflow.json", "w") as f:
    json.dump({"nodes": json_nodes}, f, indent=2)

print(f"Saved {len(json_nodes)} process nodes")
