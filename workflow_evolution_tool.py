import subprocess
import sys
import os

if len(sys.argv) != 2:
    print("Usage:")
    print("python3 workflow_evolution_tool.py <github_url>")
    sys.exit(1)

repo_url = sys.argv[1]

repo_name = repo_url.split("/")[-1]

if repo_name.endswith(".git"):
    repo_name = repo_name[:-4]

base_dir = os.getcwd()

# Clone repository if needed
if not os.path.exists(repo_name):
    print(f"Cloning {repo_url}")
    subprocess.run(["git", "clone", repo_url])

print(f"Repository: {repo_name}")

# Enter repository
os.chdir(repo_name)

print("\nRecent commits:\n")

result = subprocess.check_output(
    ["git", "log", "--oneline", "-10"],
    text=True
)

print(result)

commits = []

for line in result.splitlines():
    commits.append(line.split()[0])

print("Selected commits:")

for c in commits:
    print(c)

print("\nCurrent commit:")
subprocess.run(["git", "rev-parse", "--short", "HEAD"])

print("\nAnalyzing commits...")

# Analyze first 3 commits
for commit in commits[:3]:

    print(f"\n===== {commit} =====")

    subprocess.run(["git", "checkout", commit])

    # Remove old DAG if present
    if os.path.exists("dag.dot"):
        os.remove("dag.dot")

    # Check if repository has a test profile
    has_test_profile = False

    if os.path.exists("nextflow.config"):
        with open("nextflow.config") as f:
            if "test" in f.read():
                has_test_profile = True

    # Generate DAG
    if has_test_profile:

        print("Using test profile...")

        result = subprocess.run([
            "/home/bhoomika/nextflow",
            "run", ".",
            "-profile", "test",
            "-with-dag", "dag.dot"
        ])

    else:

        print("No test profile found. Running without test profile...")

        result = subprocess.run([
            "/home/bhoomika/nextflow",
            "run", ".",
            "-with-dag", "dag.dot"
        ])

    # If Nextflow failed, skip this commit
    if result.returncode != 0:
        print(f"Nextflow failed for commit {commit}. Skipping...")
        continue

    # Check whether DAG was created
    if os.path.exists("dag.dot"):

        print("DAG generated")

        subprocess.run([
            "python3",
            f"{base_dir}/scripts/build_graph_json.py",
            "dag.dot"
        ])

        subprocess.run([
            "cp",
            "dag_graph.json",
            f"{commit}_graph.json"
        ])

        print(f"Saved {commit}_graph.json")

    else:
        print("No DAG generated")

# Return to latest version
subprocess.run(["git", "checkout", "master"])

print("\nDone!")
print("\nGenerating evolution dataset...")

subprocess.run([
    "python3",
    f"{base_dir}/scripts/create_evolution_json.py"
])

print("\nGenerating report...")

subprocess.run([
    "python3",
    f"{base_dir}/scripts/evolution_report.py"
])
