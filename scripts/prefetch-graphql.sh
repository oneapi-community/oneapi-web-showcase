#!/bin/bash
jq -r '.[].openGraphImageUrl' data/github_repos.json | while read url; do
  curl -s -o /dev/null "$url"
done

