import subprocess

print("Step 1: Generate graphs")
subprocess.run(["python3", "scripts/repo_evolution.py"])

print("Step 2: Generate evolution dataset")
subprocess.run(["python3", "scripts/create_evolution_json.py"])

print("Step 3: Generate report")
subprocess.run(["python3", "scripts/evolution_report.py"])

print("\nDone!")
