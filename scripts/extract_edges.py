import pydot

graph = pydot.graph_from_dot_file("dag.dot")[0]

# node_id -> label
node_labels = {}

for node in graph.get_nodes():
    node_id = node.get_name()
    label = node.get_label()

    if label:
        node_labels[node_id] = label.strip('"')

edges = set()

for edge in graph.get_edges():
    src = edge.get_source()
    dst = edge.get_destination()

    src_label = node_labels.get(src)
    dst_label = node_labels.get(dst)

    if (
        src_label
        and dst_label
        and "NFCORE_" in src_label
        and "NFCORE_" in dst_label
    ):
        edges.add((src_label, dst_label))

print(f"Process edges: {len(edges)}")

for src, dst in sorted(edges):
    print(f"{src} -> {dst}")
