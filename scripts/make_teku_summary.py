import json

from bs4 import BeautifulSoup
from datetime import datetime, timezone

with open("teku/eth-reference-tests/build/reports/tests/referenceTest/index.html") as f:
    soup = BeautifulSoup(f, "html.parser")

def get_counter(id):
    box = soup.find("div", {"class": "infoBox", "id": id})
    return box.find("div", class_="counter").text.strip()

total = int(get_counter("tests"))
failed = int(get_counter("failures"))
ignored = int(get_counter("ignored"))
duration = get_counter("duration")

with open("docs/summaries/teku.json", "w") as out:
    json.dump({
        "test_status": total > 0 and failed == 0,
        "test_duration": duration,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }, out, indent=2)
