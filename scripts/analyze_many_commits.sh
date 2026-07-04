#!/bin/bash

COMMIT=$1

git checkout $COMMIT

~/nextflow run . -profile test --outdir results -with-dag dag.dot || true

python3 scripts/build_graph_json.py dag.dot

cp dag.dot ${COMMIT}.dot
cp dag_graph.json ${COMMIT}_graph.json
