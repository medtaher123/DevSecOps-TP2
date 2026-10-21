import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    data = json.load(f)

counts = {"3": 0, "2": 0, "1": 0, "0": 0}
highs = []

for site in data.get("site", []):
    for alert in site.get("alerts", []):
        code = str(alert.get("riskcode", "0"))
        counts[code] = counts.get(code, 0) + 1
        if code == "3":
            highs.append(alert)

print(
    f"ZAP summary - High: {counts['3']} | Medium: {counts['2']} | "
    f"Low: {counts['1']} | Info: {counts['0']}"
)
for alert in highs:
    print(f"  [HIGH] {alert.get('name')} ({alert.get('count', '?')} instance(s))")

sys.exit(1 if highs else 0)
