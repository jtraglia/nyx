import os
import json

from datetime import datetime, timezone

def getenv_bool(name):
    val = os.getenv(name, "").lower()
    return val == "true"

def getenv_int(name):
    try:
        return int(os.getenv(name, "0"))
    except ValueError:
        return 0

build_status = getenv_bool("BUILD_SUCCESS")
build_duration = getenv_int("BUILD_DURATION")
test_status = getenv_bool("TEST_SUCCESS") if build_status else None
test_duration = getenv_int("TEST_DURATION") if build_status else None

summary = {
    "build_status": build_status,
    "build_duration": build_duration,
    "test_status": test_status,
    "test_duration": test_duration,
    "timestamp": datetime.now(timezone.utc).isoformat(),
}

os.makedirs("docs/summaries", exist_ok=True)
with open("docs/summaries/grandine.json", "w") as out:
    json.dump(summary, out, indent=2)