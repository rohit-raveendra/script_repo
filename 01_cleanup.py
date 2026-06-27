"""01_cleanup.py — Cleanup temporary discovery artifacts.

This script executes as the first step of the Cleanup Workflow,
which is chained after the SCM Discovery workflow completes.

It simulates cleanup activities such as:

- Removing temporary workspace files
- Archiving generated reports
- Recording workflow completion

This script does not actually delete any files. Its purpose is to
demonstrate workflow chaining.

Workflow Inputs:
    {{steps.generate_summary.project}}
    {{steps.generate_summary.project_id}}
    {{steps.generate_summary.job_id}}
    {{steps.generate_summary.repository_count}}
    {{steps.generate_summary.total_size_mb}}

Output Keys:
    cleanup_status
    archived_report
    cleaned_workspace
    completed_at
"""

import json
import sys
import time
from datetime import datetime

# ---------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------

PROJECT_NAME = {{steps.generate_summary.project}}
PROJECT_ID = {{steps.generate_summary.project_id}}
JOB_ID = {{steps.generate_summary.job_id}}

REPOSITORY_COUNT = {{steps.generate_summary.repository_count}}
TOTAL_SIZE_MB = {{steps.generate_summary.total_size_mb}}

print(
    f"[cleanup] Starting cleanup workflow "
    f"(job={JOB_ID})",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

if not PROJECT_NAME:
    raise RuntimeError("Project name is missing.")

if not JOB_ID:
    raise RuntimeError("Job ID is missing.")

# ---------------------------------------------------------------------
# Simulated Cleanup
# ---------------------------------------------------------------------

print(
    "[cleanup] Archiving discovery report...",
    file=sys.stderr,
)
time.sleep(1)

report_path = (
    f"/mnt/efs/archive/{PROJECT_ID}/{JOB_ID}/discovery-summary.json"
)

print(
    "[cleanup] Cleaning temporary workspace...",
    file=sys.stderr,
)
time.sleep(1)

workspace_path = (
    f"/mnt/efs/workspaces/{JOB_ID}"
)

print(
    "[cleanup] Releasing temporary resources...",
    file=sys.stderr,
)
time.sleep(1)

print(
    "[cleanup] Cleanup completed successfully.",
    file=sys.stderr,
)

# ---------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------

print(
    json.dumps(
        {
            "cleanup_status": "SUCCESS",
            "project": PROJECT_NAME,
            "project_id": PROJECT_ID,
            "job_id": JOB_ID,
            "repositories_processed": REPOSITORY_COUNT,
            "processed_data_mb": TOTAL_SIZE_MB,
            "archived_report": report_path,
            "cleaned_workspace": workspace_path,
            "completed_at": (
                datetime.utcnow()
                .isoformat(timespec="seconds") + "Z"
            ),
        }
    )
)