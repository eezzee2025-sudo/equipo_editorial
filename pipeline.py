import yaml, json, os
from datetime import datetime

def load_settings():
    with open("config/settings.yaml") as f:
        return yaml.safe_load(f)

def run_pipeline(day):
    output = {"day": day, "status": "pending"}
    os.makedirs("queue", exist_ok=True)
    with open("queue/pending.json", "w") as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    today = datetime.now().strftime("%A").lower()
    run_pipeline(today)
