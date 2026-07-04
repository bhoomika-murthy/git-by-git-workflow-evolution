import pydot

OPERATORS = {
    "branch",
    "channel.empty",
    "channel.fromList",
    "channel.fromPath",
    "channel.of",
    "collect",
    "collectFile",
    "combine",
    "countLines",
    "distinct",
    "filter",
    "first",
    "flatten",
    "groupTuple",
    "ifEmpty",
    "join",
    "map",
    "mix",
    "splitCsv",
    "splitFasta",
    "subscribe",
    "toList",
    "toSortedList",
    "unique"
}

graph = pydot.graph_from_dot_file("dag.dot")[0]

processes = []

for node in graph.get_nodes():
    label = node.get_label()
    xlabel = node.get("xlabel")

    if label and "NFCORE_" in label:
        processes.append(label.strip('"'))

print(f"Processes found: {len(processes)}")

for p in sorted(set(processes)):
    print(p)

