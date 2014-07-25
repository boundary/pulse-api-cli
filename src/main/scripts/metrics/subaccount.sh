#!/bin/bash

curl -s -X GET -u "$BOUNDARY_USER_ID:$BOUNDARY_PASSWORD" "http://${BOUNDARY_METRICS_AUTH_HOST}/${BOUNDARY_ORG_ID}/subaccount" | jq '{email: .email, apiToken: .apiToken}'
