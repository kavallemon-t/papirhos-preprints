#!/usr/bin/env bash

set -euo pipefail

inputpath="../docs/assets/pdfs_src/"
outputpath="../docs/assets/covers/"

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 input.pdf" >&2
	exit 2
fi

pdf="${inputpath}$1"
# pdf=$1
if [[ ! -f "$pdf" ]]; then
	echo "File not found: $pdf" >&2
	exit 1
fi

output="${pdf%.*}"
pdftoppm -f 1 -l 1 -r 300 -png "$pdf" "$output"

mv "${output}-001.png" "${outputpath}${1%.*}.png"

# echo "Cover page extracted to ${output}-001.png"