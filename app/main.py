import os
from datetime import datetime, timezone

def build_info() -> dict:
    return {
        "app": "git-workflow-to-prod",
        "env": os.getenv("APP_ENV", "local"),
        "git_sha": os.getenv("GIT_SHA", "unknown"),
        "built_at_utc": os.getenv("BUILT_AT_UTC", "unknown"),
        "now_utc": datetime.now(timezone.utc).isoformat(),
    }

def main() -> None:
    info = build_info()
    for k, v in info.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
