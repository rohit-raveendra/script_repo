"""03_discover_branches.py — Discover branches for repositories.

This script simulates branch discovery for repositories identified
by the discovery step. It is intended to execute in parallel with
discover_contributors.py.

Input:
    {{steps.discover_repositories.repositories}}

Workflow Inputs:
    {{steps.init.project_id}}
    {{steps.init.job_id}}

Output Keys:
    branches
    total_branches
"""

import json
import sys
import time

# ---------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------

REPOSITORIES = {{steps.discover_repositories.repositories}}
PROJECT_ID = {{steps.init.project_id}}
JOB_ID = {{steps.init.job_id}}

print(
    f"[discover_branches] Starting branch discovery "
    f"(job={JOB_ID}, project={PROJECT_ID})",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Simulated Branch Discovery
# ---------------------------------------------------------------------

branches = {}
total_branches = 0

for repository in REPOSITORIES:

    repo_name = repository["name"]

    print(
        f"[discover_branches] Discovering branches for {repo_name}",
        file=sys.stderr,
    )

    # Simulate API latency
    time.sleep(0.5)

    # Deterministic branch generation
    if repository["repository_type"] == "Application":
        repo_branches = [
            "main",
            "develop",
            "release",
        ]

    elif repository["repository_type"] == "Library":
        repo_branches = [
            "main",
            "develop",
        ]

    else:
        repo_branches = [
            "main",
            "feature/demo",
            "release",
            "hotfix",
        ]

    branches[repo_name] = repo_branches
    total_branches += len(repo_branches)

    print(
        f"[discover_branches] "
        f"{repo_name}: {len(repo_branches)} branches discovered",
        file=sys.stderr,
    )

print(
    f"[discover_branches] "
    f"Completed branch discovery. "
    f"Repositories={len(REPOSITORIES)}, "
    f"Branches={total_branches}",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(
    json.dumps(
        {
            "branches": branches,
            "total_branches": total_branches,
        }
    )
)