#!/bin/env python3
import sys
import os

# ANNOTATION_1=file=README.md,line=2,endLine=2,title='No content'::Read me is empty and should be filled.\nit should have more details.
# ANNOTATION_2=file=.github/workflows/linter.yml,line=30,endLine=33,title='annotation'::HELLO tests2

# loop for environment variables and find variable  starts with ANNOTATION_
for env in os.environ:
    if env.startswith("ANNOTATION_"):
        print("")
        print(f"::notice {os.environ[env]}")

print("Finished")
