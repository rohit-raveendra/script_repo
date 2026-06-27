"""06_generate_summary.py — Generate SCM discovery summary.

This script aggregates the outputs produced by previous workflow
steps and generates a final SCM discovery report.

Inputs:
    {{steps.init.project_name}}
    {{steps.init.discovery_mode}}
    {{steps.init.project_id}}
    {{steps.init.job_id}}

    {{steps.discover_repositories.repositories}}
    {{steps.discover_branches.branches}}
    {{steps.discover_contributors.contributors}}
    {{steps.analyze_repository.analysis}}

Output Keys:
    project
    repository_count
    total_branches
    total_contributors
    total_commits
    total_files
    total_size_mb
    average_health_score
    repositories
    summary_generated_at
"""

import json
import sys
from datetime import datetime

# ---------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------

PROJECT_NAME = {{steps.init.project_name}}
DISCOVERY_MODE = {{steps.init.discovery_mode}}
PROJECT_ID = {{steps.init.project_id}}
JOB_ID = {{steps.init.job_id}}

REPOSITORIES = {{steps.discover_repositories.repositories}}
BRANCHES = {{steps.discover_branches.branches}}
CONTRIBUTORS = {{steps.discover_contributors.contributors}}

# Result accumulated from LOOP executions
ANALYSIS = {{steps.analyze_repository.analysis}}

print(
    f"[generate_summary] Building discovery summary "
    f"(job={JOB_ID})",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Aggregate Metrics
# ---------------------------------------------------------------------

total_branches = 0
total_contributors = 0
total_commits = 0
total_files = 0
total_size_mb = 0
total_health_score = 0

repository_summary = []

for repository in REPOSITORIES:

    repo_name = repository["name"]

    analysis = next(
        item
        for item in ANALYSIS
        if item["repository"] == repo_name
    )

    repo_branches = BRANCHES.get(repo_name, [])
    repo_contributors = CONTRIBUTORS.get(repo_name, [])

    total_branches += len(repo_branches)
    total_contributors += len(repo_contributors)
    total_commits += analysis["commit_count"]
    total_files += analysis["file_count"]
    total_size_mb += analysis["size_mb"]
    total_health_score += analysis["health_score"]

    repository_summary.append(
        {
            "repository": repo_name,
            "language": analysis["language"],
            "repository_type": repository["repository_type"],
            "branches": len(repo_branches),
            "contributors": len(repo_contributors),
            "commits": analysis["commit_count"],
            "files": analysis["file_count"],
            "size_mb": analysis["size_mb"],
            "health_score": analysis["health_score"],
        }
    )

average_health_score = round(
    total_health_score / len(REPOSITORIES),
    2,
)

print(
    f"[generate_summary] Summary generated successfully.",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(
    json.dumps(
        {
            "project": PROJECT_NAME,
            "discovery_mode": DISCOVERY_MODE,
            "project_id": PROJECT_ID,
            "job_id": JOB_ID,
            "repository_count": len(REPOSITORIES),
            "total_branches": total_branches,
            "total_contributors": total_contributors,
            "total_commits": total_commits,
            "total_files": total_files,
            "total_size_mb": total_size_mb,
            "average_health_score": average_health_score,
            "repositories": repository_summary,
            "summary_generated_at": (
                datetime.utcnow()
                .isoformat(timespec="seconds") + "Z"
            ),
        }
    )
)