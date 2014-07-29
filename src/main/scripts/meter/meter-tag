#!/bin/bash
if [ $# -ne 2 ]
then
   echo "usage: $(basename $0) meter_id tag"
   exit 1
fi
typeset -r meter_id=$1
# TODO: Use shift to have additional tags
typeset -r tag=$2

curl -X PUT -i -u "${BOUNDARY_API_KEY}": -H "Content-Type: application/json" -d '{}' "https://api.boundary.com/${BOUNDARY_ORG_ID}/meters/${meter_id}/tags/${tag}"
