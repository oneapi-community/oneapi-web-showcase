# Ensure this script fails on error
set shell := ["bash", "-cu"]

# Environment variables (optional)
set dotenv-load := true

# Warm GitHub OpenGraph cache
warm-cache:
  echo "Running OpenGraph prefetch..."
  ./scripts/warm-graph-images.sh

# Build the site using Hugo
build:
  just warm-cache
  hugo

# Clean all generated files
clean:
  rm -rf public resources

# Preview locally
serve:
  hugo server --buildDrafts --buildFuture --disableFastRender
