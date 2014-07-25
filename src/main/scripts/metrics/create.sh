#!/bin/bash

curl -X PUT -u <email>:<api-token> \
-H "Content-Type: application/json" \
-d '
{
   "name": "MY_COOL_METRIC",
   "description": "A cool metric I created",
   "displayName": "My cool metric",
   "displayNameShort": "cool metric",
   "unit": "number",
   "defaultAggregate": "avg"
}'
https://$BOUNDARY_API_METRICS_HOST/v1/metrics/ \
