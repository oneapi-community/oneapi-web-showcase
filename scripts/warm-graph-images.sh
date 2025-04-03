#!/bin/bash
#
# This is a script that will make sure that OpenGraph images are available for our target repos.
# Then we can download those images and ensure that we always have images.
#
#
set -e

echo "Warming GitHub OpenGraph cache..."

# Adjust path if needed
DATA_FILE="data/github_repos.json"

# Extract all OpenGraph image URLs and hit them with curl
jq -r '.[].openGraphImageUrl' "$DATA_FILE" | while read -r url; do
  echo "Warming $url"
  curl -s -o /dev/null "$url"
done

echo "Done warming OpenGraph images."
