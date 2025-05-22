import os
import json

from datetime import datetime, timezone

def getenv_bool(name):
    val = os.getenv(name, "").lower()
    return val == "true"

def getenv_float(name):
    try:
        return float(os.getenv(name, "0"))
    except ValueError:
        return 0

def format_duration(seconds: float) -> str:
    mins = int(seconds // 60)
    secs = seconds % 60
    if mins > 0:
        return f"{mins}m{secs:05.2f}s"
    else:
        return f"{secs:.2f}s"

test_status = getenv_bool("TEST_SUCCESS")
test_duration = getenv_float("TEST_DURATION")

summary = {
    "test_status": test_status,
    "test_duration": format_duration(test_duration),
    "timestamp": datetime.now(timezone.utc).isoformat(),
}

os.makedirs("docs/summaries", exist_ok=True)
with open("docs/summaries/prysm.json", "w") as out:
    json.dump(summary, out, indent=2)