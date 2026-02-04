#!/bin/bash
# Usage: ./run.sh [logfile] [csvfile] [options]
python3 convert_nginx_log.py "$@"

# Add CSV file to git and commit
csvfile="$2"
git add "$csvfile"
git commit -m "Add CSV export from nginx log: $csvfile"
