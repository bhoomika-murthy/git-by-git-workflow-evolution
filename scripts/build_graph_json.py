import json
import pydot
import sys

dotfile = sys.argv[1]

graph = pydot.graph_from_dot_file(dotfile)[0]

node_labels = {}

all_nodes = {}

for node in graph.get_nodes():

    node_id = node.get_name()
    label = node.get_label()

    if label:
        clean_label = label.strip('"')
    else:
        clean_label = ""

    all_nodes[node_id] = clean_label

    if clean_label != "":
        node_labels[node_id] = clean_label

nodes = sorted(set(node_labels.values()))

adj = {}

for edge in graph.get_edges():

    src = edge.get_source()
    dst = edge.get_destination()

    adj.setdefault(src, []).append(dst)

links = []
seen = set()

for process_node in node_labels:

    stack = [process_node]
    visited = set()

    while stack:

        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        for nxt in adj.get(current, []):

            if nxt in node_labels and nxt != process_node:

                edge_pair = (
                    node_labels[process_node],
                    node_labels[nxt]
                )

                if edge_pair not in seen:

                    seen.add(edge_pair)

                    links.append({
                        "source": edge_pair[0],
                        "target": edge_pair[1]
                    })

            else:
                stack.append(nxt)

data = {
    "nodes": [{"id": n} for n in nodes],
    "links": links
}

outfile = dotfile.replace(".dot", "_graph.json")

with open(outfile, "w") as f:
    json.dump(data, f, indent=2)

print(f"Nodes: {len(nodes)}")
print(f"Links: {len(links)}")
print(f"Saved: {outfile}")
