#!/usr/bin/env bash

set -ue

CRONFILE="famous.crontab"

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Build docker-compose images..."
docker compose build


# Create the file if it doesn't exist
touch "$CRONFILE"

# Merge existing crontab with the file, remove duplicates, and reload
(
  crontab -l 2>/dev/null
  cat "$CRONFILE"
) | sort -u | crontab -
