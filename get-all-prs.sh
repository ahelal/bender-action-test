#!/bin/bash
set -e 

echo "* Running $0 script"

doGitHubAPI(){
  curl -Ls \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    'https://api.github.com/repos/ahelal/bender-action-test/pulls'
}

echo "* Getting all PRs"
# doGitHubAPI | jq -r ".[] | [.title, .number] | @tsv"
# exit 0

doGitHubAPI | jq -r ".[] | [.title, .number] | @tsv"| while IFS=$'\t' read -r title number; do
    echo "${number}-${title}"
    touch pr/"${title}" 2> /dev/null
done 
