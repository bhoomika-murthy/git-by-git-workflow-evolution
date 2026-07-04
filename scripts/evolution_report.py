import json

with open("evolution.json") as f:
    data = json.load(f)

print("\nWorkflow Evolution Report\n")

for item in data:
    print(
        f"{item['commit']} : "
        f"{item['nodes']} nodes, "
        f"{item['edges']} edges"
    )

max_nodes = max(data, key=lambda x: x["nodes"])
min_nodes = min(data, key=lambda x: x["nodes"])

print("\nLargest workflow:")
print(max_nodes)

print("\nSmallest workflow:")
print(min_nodes)
