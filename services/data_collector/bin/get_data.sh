#!/bin/bash

# Cleaning old file
rm -f $DATADIR/downloaded.csv.gz

# Curl -L to follow redirections because url does not lead directly to archive
# https://explainshell.com/explain?cmd=curl+-L+https%3A%2F%2Fwww.data.gouv.fr%2Ffr%2Fdatasets%2Fr%2Facc332f6-92be-42af-9721-f3609bea8cfc+%3E+%22%24DATADIR%2Fdownloaded.csv.gz%22#
curl -L https://www.data.gouv.fr/fr/datasets/r/acc332f6-92be-42af-9721-f3609bea8cfc > "$DATADIR/downloaded.csv"

cd "$DATADIR"

# gunzip -f downloaded.csv.gz
mv downloaded.csv "$DOWNLOADED_FILE"

# Check encoding and switch encoding if necessary
RESULT_FILE_CMD=$(file "$DOWNLOADED_FILE")
if echo "$RESULT_FILE_CMD" | grep -q ISO-8859; then
    # https://explainshell.com/explain?cmd=iconv+-f+ISO-8859-1+-t+UTF-8+%22%24DOWNLOADED_FILE%22+-o+%22%24DOWNLOADED_FILE.utf8%22
    iconv -f ISO-8859-1 -t UTF-8 "$DOWNLOADED_FILE" -o "$DOWNLOADED_FILE.utf8"
    mv "$DOWNLOADED_FILE.utf8" "$DOWNLOADED_FILE"
    echo "✅ Data encoding switched to UTF-8"
fi
