import json

with open("inquiries.json", encoding="utf-8") as f:
    answers = {i["id"]: i for i in json.load(f)}
with open("results.json", encoding="utf-8") as f:
    results = json.load(f)

auto = [r for r in results if r["team"] != "human"]

guess_ok = sum(r["team_guess"] == answers[r["id"]]["team"] for r in results)
auto_ok = sum(r["team"] == answers[r["id"]]["team"] for r in auto)
urgent_ok = sum(r["urgent"] == answers[r["id"]]["urgent"] for r in results)

print("Team guesses correct (all):", guess_ok, "/", len(results))
print("Routed automatically:", len(auto), "/", len(results))
print("Correct among auto-routed:", auto_ok, "/", len(auto))
print("Sent to a human:", len(results) - len(auto))
print("Urgency calls correct:", urgent_ok, "/", len(results))

print("Mistakes:")
for r in results:
    a = answers[r["id"]]
    if r["team_guess"] != a["team"] or r["urgent"] != a["urgent"]:
        print(
            r["id"],
            "team", r["team_guess"], "expected", a["team"],
            "confidence", round(r["confidence"], 2),
            "urgent", r["urgent"], "expected", a["urgent"],
        )
