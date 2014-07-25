#!/bin/bash

if [ $# -ne 1 ]
then
   echo "usage: $(basename $0) name"
   exit 1
fi
typeset -r meter_name=$1

curl -X POST -u "${BOUNDARY_API_KEY}": -H "Content-Type: application/json" -d "{\"name\": \"$meter_name\"}" "https://api.boundary.com/${BOUNDARY_ORG_ID}/meters" | jq '.'
