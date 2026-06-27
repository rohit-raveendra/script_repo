"""02_discover_repositories.py — Discover repositories for a project.

This script simulates repository discovery from an SCM system.

It reads the workflow context from the init step and generates a
deterministic list of repositories. The output is consumed by
parallel discovery scripts and the repository analysis loop.

Downstream scripts use:

    {{steps.discover_repositories.repositories}}

Placeholders:
    {{steps.init.project_name}}      - Project name
    {{steps.init.discovery_mode}}    - FULL or QUICK discovery
    {{steps.init.repository_count}}  - Number of repositories
    {{steps.init.project_id}}        - Project identifier
    {{steps.init.job_id}}            - Workflow execution id

Output Keys:
    repositories
    discovered_count
"""

import json
import sys
import time

# ---------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------

PROJECT_NAME = {{steps.init.project_name}}
DISCOVERY_MODE = {{steps.init.discovery_mode}}
REPOSITORY_COUNT = {{steps.init.repository_count}}
PROJECT_ID = {{steps.init.project_id}}
JOB_ID = {{steps.init.job_id}}

print(
    f"[discover_repositories] Starting repository discovery "
    f"(job={JOB_ID})",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Simulate discovery
# ---------------------------------------------------------------------

languages = [
    "Python",
    "Java",
    "Go",
    "C#",
    "JavaScript",
    "TypeScript",
    "C++",
]

repository_types = [
    "Application",
    "Library",
    "Microservice",
]

repositories = []

for index in range(REPOSITORY_COUNT):

    # simulate work
    time.sleep(0.5)

    repo = {
        "id": f"repo-{index + 1}",
        "name": f"{PROJECT_NAME.lower().replace(' ', '-')}-repo-{index + 1}",
        "language": languages[index % len(languages)],
        "default_branch": "main",
        "repository_type": repository_types[
            index % len(repository_types)
        ],
        "archived": False,
    }

    repositories.append(repo)

    print(
        f"[discover_repositories] Discovered {repo['name']}",
        file=sys.stderr,
    )

# ---------------------------------------------------------------------
# Discovery summary
# ---------------------------------------------------------------------

print(
    f"[discover_repositories] "
    f"Discovery completed. "
    f"Repositories found: {len(repositories)}",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(
    json.dumps(
        {
            "repositories": repositories,
            "discovered_count": len(repositories),
        }
    )
)