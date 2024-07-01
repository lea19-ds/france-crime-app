#!/bin/bash

cd ../app/

python3 processor.py "$CLEANED_FILE" "$PROCESSED_FILE"
