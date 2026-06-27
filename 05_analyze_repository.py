"""05_analyze_repository.py — Analyze a single repository.

This script is intended to execute as a LOOP activity.

The workflow engine should iterate over the repository list produced
by discover_repositories.py and invoke this script once for each
repository.

Input:
    {{previous}}

Workflow Inputs:
    {{steps.init.discovery_mode}}
    {{steps.init.project_id}}
    {{steps.init.job_id}}

Output Keys:
    repository
    language
    branch_count
    contributor_count
    commit_count
    file_count
    size_mb
    health_score
"""

import json
import sys
import time

# ---------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------

# During loop execution the workflow engine passes one repository object
# from discover_repositories.repositories.
#
# Example:
# {
#     "id":"repo-1",
#     "name":"scm-demo-repo-1",
#     "language":"Python",
#     "default_branch":"main",
#     "repository_type":"Application",
#     "archived":False
# }

REPOSITORY = {{previous}}

DISCOVERY_MODE = {{steps.init.discovery_mode}}
PROJECT_ID = {{steps.init.project_id}}
JOB_ID = {{steps.init.job_id}}

print(
    f"[analyze_repository] "
    f"Analyzing {REPOSITORY['name']} "
    f"(job={JOB_ID})",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Simulate repository analysis
# ---------------------------------------------------------------------

time.sleep(1)

language = REPOSITORY["language"]
repo_type = REPOSITORY["repository_type"]

# Produce deterministic metrics based on repository type.

if repo_type == "Application":

    branch_count = 3
    contributor_count = 6
    commit_count = 1542
    file_count = 4820
    size_mb = 285
    health_score = 96

elif repo_type == "Library":

    branch_count = 2
    contributor_count = 4
    commit_count = 874
    file_count = 1625
    size_mb = 74
    health_score = 92

else:

    branch_count = 4
    contributor_count = 8
    commit_count = 2380
    file_count = 7210
    size_mb = 510
    health_score = 89

print(
    f"[analyze_repository] "
    f"{REPOSITORY['name']} analysis completed.",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(
    json.dumps(
        {
            "repository": REPOSITORY["name"],
            "language": language,
            "branch_count": branch_count,
            "contributor_count": contributor_count,
            "commit_count": commit_count,
            "file_count": file_count,
            "size_mb": size_mb,
            "health_score": health_score,
        }
    )
)