#!/bin/env python3
import os
import re
import json
import requests
from pathlib import Path
import frontmatter

GH_TOKEN = os.getenv("GH_TOKEN")
GRAPHQL_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": f"Bearer {GH_TOKEN}"}

HUGO_CONTENT_DIR = "content/projects"
OUTPUT_JSON_PATH = "data/github_repos.json"

def extract_repos_from_content():
    repos = []
    for mdfile in Path(HUGO_CONTENT_DIR).rglob("*.md"):
        print("mdfile is", mdfile)
        post = frontmatter.load(mdfile)
        github_url = post.get("githublink")
        if github_url:
            match = re.match(r"https?://github.com/([^/]+)/([^/]+)", github_url)
            if match:
                owner, name = match.groups()
                repos.append((owner, name))
    return repos

QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    name
    description
    url
    updatedAt
    openGraphImageUrl
  }
}
"""

def fetch_repo_metadata(repos):
    results = []
    for owner, name in repos:
        resp = requests.post(
            GRAPHQL_URL,
            headers=HEADERS,
            json={"query": QUERY, "variables": {"owner": owner, "name": name}}
        )
        data = resp.json().get("data", {}).get("repository")
        if data:
            print("data is", data)
            results.append(data)
    return results

if __name__ == "__main__":
    repos = extract_repos_from_content()
    repo_data = fetch_repo_metadata(repos)
    with open(OUTPUT_JSON_PATH, "w") as f:
        json.dump(repo_data, f, indent=2)
    print(f"Fetched metadata for {len(repo_data)} repos.")

