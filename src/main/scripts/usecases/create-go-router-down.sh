#/bin/bash
SCRIPT_PATH="${BASH_SOURCE[0]}"
curl -X POST http://localhost:8080/ChMBk5Ou9QBdDPaTai0rfUbZ8bC/triangulation/rules -d @"$(dirname $SCRIPT_PATH)/rules/go-router-down.json" -H "Content-Type: application/json" --verbose
