"""01_init.py — Initialize the SCM Discovery workflow.

This script validates all workflow-wide inputs and forwards them to
subsequent scripts. It serves as the single source of truth for
workflow parameters.

Every downstream script should reference values from this script using:

    {{steps.init.<key>}}

instead of declaring duplicate placeholders.

Placeholders:
    {{PROJECT_NAME}}      - Display name of the project
    {{DISCOVERY_MODE}}    - Discovery mode (FULL or QUICK)
    {{REPOSITORY_COUNT}}  - Number of repositories to simulate
    {{PROJECT_ID}}        - Correlation project identifier
    {{EXECUTION_ID}}      - Auto injected execution identifier

Output Keys:
    project_name
    discovery_mode
    repository_count
    project_id
    job_id
    started_at
"""

import json
import sys
from datetime import datetime

# ---------------------------------------------------------------------
# Workflow Inputs
# ---------------------------------------------------------------------

PROJECT_NAME = {{PROJECT_NAME}}
DISCOVERY_MODE = {{DISCOVERY_MODE}}
REPOSITORY_COUNT = {{REPOSITORY_COUNT}}
PROJECT_ID = {{PROJECT_ID}}
JOB_ID = {{EXECUTION_ID}}

# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

print(f"[init] Starting workflow {JOB_ID}", file=sys.stderr)

if not PROJECT_NAME:
    raise RuntimeError("PROJECT_NAME cannot be empty.")

if DISCOVERY_MODE not in ("FULL", "QUICK"):
    raise RuntimeError(
        f"DISCOVERY_MODE must be FULL or QUICK. Received: {DISCOVERY_MODE}"
    )

if not isinstance(REPOSITORY_COUNT, int):
    raise RuntimeError("REPOSITORY_COUNT must be an integer.")

if REPOSITORY_COUNT <= 0:
    raise RuntimeError("REPOSITORY_COUNT must be greater than zero.")

if REPOSITORY_COUNT > 50:
    raise RuntimeError(
        "REPOSITORY_COUNT should not exceed 50 for the sample workflow."
    )

if not PROJECT_ID:
    raise RuntimeError("PROJECT_ID cannot be empty.")

print(f"[init] Project        : {PROJECT_NAME}", file=sys.stderr)
print(f"[init] Discovery Mode : {DISCOVERY_MODE}", file=sys.stderr)
print(f"[init] Repository Cnt : {REPOSITORY_COUNT}", file=sys.stderr)
print(f"[init] Project Id     : {PROJECT_ID}", file=sys.stderr)

# ---------------------------------------------------------------------
# Build workflow context
# ---------------------------------------------------------------------

workflow_context = {
    "project_name": PROJECT_NAME,
    "discovery_mode": DISCOVERY_MODE,
    "repository_count": REPOSITORY_COUNT,
    "project_id": PROJECT_ID,
    "job_id": JOB_ID,
    "started_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
}

print(
    f"[init] Workflow initialization completed successfully.",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(json.dumps(workflow_context))