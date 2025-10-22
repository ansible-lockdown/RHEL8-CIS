#!/bin/bash
set -euo pipefail

# Set the location and search string
var_file=$(ggrep -Po '^(?![[:blank:]]*#)[^:]+:' defaults/main.yml | cut -d':' -f1 )

## loop over each line
while IFS= read -r var; do
    # 3. Search the two directories for the variable name.
    #    `!` is the “not” of the exit status.
    if ! grep -rl "$var" tasks templates handlers&>/dev/null; then
        echo "No Variable matching $var"
    fi
done <<< "$var_file"
