import subprocess
import os

with open("milestone_commits.txt") as f:
    commits = [line.strip() for line in f if line.strip()]

print("Commits to analyze:")
for c in commits:
    print(c)

for commit in commits:

    print(f"\n===== {commit} =====")

    # remove old DAG first
    if os.path.exists("dag.dot"):
        os.remove("dag.dot")

    subprocess.run(["git", "checkout", commit])

    subprocess.run([
        "/home/bhoomika/nextflow",
        "run", ".",
        "-profile", "test",
        "--outdir", "results",
        "-with-dag", "dag.dot"
    ])

    # what matters is whether DAG exists
    if not os.path.exists("dag.dot"):
        print(f"NO DAG GENERATED: {commit}")
        continue

    subprocess.run([
        "python3",
        "scripts/build_graph_json.py",
        "dag.dot"
    ])

    subprocess.run([
        "cp",
        "dag_graph.json",
        f"{commit}_graph.json"
    ])

subprocess.run(["git", "checkout", "master"])
