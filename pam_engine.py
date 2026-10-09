
from datetime import datetime, timedelta, timezone
import json
import uuid
from pathlib import Path

AUDIT_FILE = Path("evidence/audit.jsonl")

USERS = {
    "rahul": "engineer",
    "priya": "auditor",
    "aman": "pam_admin",
}

RESOURCE_POLICIES = {
    "production_server": {"engineer", "pam_admin"},
    "audit_logs": {"auditor", "pam_admin"},
    "pam_policies": {"pam_admin"},
}


def write_audit(event):
    """Append an event to the local audit trail."""
    AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with AUDIT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")


def request_access(
    username,
    resource,
    approved=False,
    duration_minutes=30,
):
    """Simulate a privileged-access policy decision."""

    now = datetime.now(timezone.utc)
    role = USERS.get(username)
    request_id = str(uuid.uuid4())

    allowed = False
    reason = "Access denied"
    expires_at = None

    if role is None:
        reason = "Unknown user"

    elif resource not in RESOURCE_POLICIES:
        reason = "Unknown resource"

    elif role not in RESOURCE_POLICIES[resource]:
        reason = "Role not authorized for resource"

    elif approved is not True:
        reason = "Approval required"

    elif (
        type(duration_minutes) is not int
        or not 1 <= duration_minutes <= 60
    ):
        reason = "Invalid duration: must be 1–60 minutes"

    else:
        allowed = True
        reason = "Policy checks passed"
        expires_at = (
            now + timedelta(minutes=duration_minutes)
        ).isoformat()

    event = {
        "request_id": request_id,
        "timestamp": now.isoformat(),
        "username": username,
        "role": role,
        "resource": resource,
        "approved": approved,
        "duration_minutes": duration_minutes,
        "expires_at": expires_at,
        "decision": "ALLOW" if allowed else "DENY",
        "reason": reason,
    }

    write_audit(event)
    print(json.dumps(event, indent=2))

    return event


def is_access_active(event, now=None):
    """Check whether a simulated access grant is still valid."""
    if event.get("decision") != "ALLOW":
        return False

    expires_at = event.get("expires_at")
    if not expires_at:
        return False

    expiry = datetime.fromisoformat(expires_at)

    if expiry.tzinfo is None:
        return False

    if now is None:
        now = datetime.now(timezone.utc)

    return now < expiry

if __name__ == "__main__":
    print("\n--- PAM Security Lab ---\n")

    request_access(
        "rahul", "production_server",
        approved=True, duration_minutes=30
    )

    request_access(
        "priya", "production_server",
        approved=True, duration_minutes=30
    )

    request_access(
        "rahul", "production_server",
        approved=False, duration_minutes=30
    )
