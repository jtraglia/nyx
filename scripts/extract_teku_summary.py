import json

from bs4 import BeautifulSoup

with open("teku/eth-reference-tests/build/reports/tests/referenceTest/index.html") as f:
    soup = BeautifulSoup(f, "html.parser")

def get_counter(id):
    box = soup.find("div", {"class": "infoBox", "id": id})
    return box.find("div", class_="counter").text.strip()

total = int(get_counter("tests"))
failed = int(get_counter("failures"))
ignored = int(get_counter("ignored"))
duration = get_counter("duration")

with open("docs/results/teku.json", "w") as out:
    json.dump({
        "total": total,
        "failed": failed,
        "ignored": ignored,
        "passed": total - failed - ignored,
        "duration": duration
    }, out, indent=2)