# Git-by-Git: Evolution of Scientific Workflows

## Overview

Git-by-Git is an automated workflow analysis tool developed as part of a Communication Networks Lab project at Technische Universität Darmstadt.

The project analyzes the evolution of scientific workflows across Git repository commits by automatically extracting workflow Directed Acyclic Graphs (DAGs), comparing workflow versions, identifying structural changes, and generating interactive visualizations.

The objective is to simplify workflow evolution analysis and reduce the manual effort required to understand changes introduced over a repository's history.

---

## Motivation

Scientific workflows evolve continuously as researchers modify pipelines, introduce new processing steps, and optimize existing analyses. Tracking these changes manually is time-consuming and error-prone.

This project automates the complete workflow analysis pipeline, making workflow evolution easier to understand and reproduce.

---

## Features

- Automatic Git repository traversal
- Workflow extraction from multiple commits
- DAG generation using Nextflow
- Graph cleaning and simplification
- Workflow comparison between commits
- Detection of added and removed workflow nodes
- JSON generation for visualization
- Interactive D3.js visualization
- Evolution summary generation
- Support for multiple nf-core workflows

---

## Technologies

- Python
- Bash
- Nextflow
- Graphviz
- D3.js
- HTML
- JavaScript
- JSON
- Git

---

## Repository Structure

```text
scripts/                 Python automation scripts
docs/                    Documentation
assets/                  Supporting resources
workflows/               Workflow files
subworkflows/            Extracted workflow components
index.html               Interactive visualization
README.md
LICENSE
```

---

## Workflow

1. Traverse the Git repository history.
2. Generate workflow DAGs using Nextflow.
3. Clean generated workflow graphs.
4. Compare workflow structures between commits.
5. Generate JSON representations.
6. Produce workflow evolution reports.
7. Visualize workflow evolution using D3.js.

---

## My Contribution

During this project, I:

- Developed Python scripts to automate workflow extraction.
- Implemented graph processing and comparison utilities.
- Automated workflow evolution analysis across Git commits.
- Generated JSON data for D3.js visualizations.
- Integrated Nextflow and Graphviz outputs into a unified workflow analysis pipeline.
- Contributed to the design of an automated workflow evolution framework.

---

## Future Work

Future improvements may include:

- Support for additional workflow management systems.
- More advanced workflow comparison metrics.
- Performance optimization for large repositories.
- Enhanced visualization features.
- Improved support for historical workflow reconstruction.

---

## Author

**Bhoomika Murthy**

M.Sc. Information & Communication Engineering

Technische Universität Darmstadt
