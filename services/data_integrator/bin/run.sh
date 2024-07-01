#!/bin/bash

if test -f "$DOWNLOADED_FILE"; then
  echo "🗃️ $DOWNLOADED_FILE exists. Launching integration"
  bash clean.sh
  echo "✅ Data integration succeeded"
else
  echo "🛑 No raw file detected"
fi
