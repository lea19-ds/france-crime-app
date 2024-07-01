#!/bin/bash

if test -f "$PROCESSED_FILE"; then
    echo "🗃️ $PROCESSED_FILE exists. Launching web application"
    bash webapp.sh
else
  echo "🛑 No processed file detected"
fi