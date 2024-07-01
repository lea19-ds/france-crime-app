#!/bin/bash

if test -f "$CLEANED_FILE"; then
  echo "🗃️ $CLEANED_FILE exists. Launching process"
  bash process.sh
  echo "✅ Data processing succeeded"
else
  echo "🛑 No cleaned file detected"
fi
