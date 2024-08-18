#!/bin/bash
set -e 

echo "* Running $0 script"

# Check dependencies
jq --version > /dev/null || (echo "jq is required" && exit 1)
curl --version > /dev/null || (echo "curl is required" && exit 1)

get_prs_from_gh(){
  curl -Ls \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    'https://api.github.com/repos/ahelal/bender-action-test/pulls'
}

echo "* Getting all PRs"

get_prs_from_gh | jq -r ".[] | [.title, .number] | @tsv"| while IFS=$'\t' read -r title number; do
    # co
    file_to_touch="pr/${number}-${title}"
    echo "Creating file '${file_to_touch}'"
    # Touch PR name locally to keep track of PRs
    touch "${file_to_touch}" 2> /dev/null
done 
