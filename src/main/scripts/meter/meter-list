#!/bin/bash
#if [ $# -ne 2 ]
#then
#   echo "usage: $(basename $0) [meter_id]"
#   exit 1
#fi
#typeset -r meter_id=$1
# TODO: Use shift to have additional tags
#typeset -r tag=$2

if [ $# -eq 1 ]
then
   URL="https://api.boundary.com/${BOUNDARY_ORG_ID}/meters/$1"
else
   URL="https://api.boundary.com/${BOUNDARY_ORG_ID}/meters"
fi

curl -s -X GET -u "${BOUNDARY_API_KEY}": -H "Content-Type: application/json" "$URL" | jq '.'
