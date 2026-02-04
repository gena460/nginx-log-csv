#!/bin/bash
set -e

python3 convert_nginx_log.py "$@"
git add "$2"
git commit -m "Add/Update CSV nginx log export: $2"
