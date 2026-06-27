"""04_discover_contributors.py — Discover repository contributors.

This script simulates discovering contributor information for each
repository identified during the repository discovery step.

This script is designed to execute in parallel with
discover_branches.py.

Workflow Inputs:
    {{steps.discover_repositories.repositories}}
    {{steps.init.project_id}}
    {{steps.init.job_id}}

Output Keys:
    contributors
    total_contributors
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
    f"[discover_contributors] Starting contributor discovery "
    f"(job={JOB_ID}, project={PROJECT_ID})",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Simulated Contributor Discovery
# ---------------------------------------------------------------------

contributors = {}
total_contributors = 0

# Deterministic contributor names
developer_pool = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Frank",
    "Grace",
    "Henry",
    "Isabella",
    "Jack",
]

for index, repository in enumerate(REPOSITORIES):

    repo_name = repository["name"]

    print(
        f"[discover_contributors] Discovering contributors for {repo_name}",
        file=sys.stderr,
    )

    # Simulate API latency
    time.sleep(0.5)

    # Produce deterministic contributor counts
    contributor_count = (index % 4) + 2

    repo_contributors = []

    for i in range(contributor_count):
        repo_contributors.append(
            {
                "name": developer_pool[(index + i) % len(developer_pool)],
                "commits": (i + 1) * 25,
            }
        )

    contributors[repo_name] = repo_contributors
    total_contributors += contributor_count

    print(
        f"[discover_contributors] "
        f"{repo_name}: {contributor_count} contributors discovered",
        file=sys.stderr,
    )

print(
    f"[discover_contributors] "
    f"Completed contributor discovery. "
    f"Repositories={len(REPOSITORIES)}, "
    f"Contributors={total_contributors}",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(
    json.dumps(
        {
            "contributors": contributors,
            "total_contributors": total_contributors,
        }
    )
)