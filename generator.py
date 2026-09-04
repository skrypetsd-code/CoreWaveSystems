import subprocess
import os
import random
from datetime import datetime, timedelta

start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 6, 4)

commit_messages = [
    "refactor: clean up legacy code in core module",
    "fix: resolve minor bug in api response handling",
    "feat: add validation logic for user input",
    "chore: update dependencies",
    "fix: handle null pointer exception in service layer"
]

current_date = start_date
while current_date <= end_date:
    if current_date.weekday() < 5 and random.random() > 0.2:
        num_commits = random.randint(1, 6)
        for _ in range(num_commits):
            h, m, s = random.randint(10, 18), random.randint(0, 59), random.randint(0, 59)
            commit_date = current_date.replace(hour=h, minute=m, second=s).strftime('%Y-%m-%dT%H:%M:%S')
            msg = random.choice(commit_messages)

            with open("history.txt", "a") as f:
                f.write(f"[{commit_date}] {msg}\n")

            subprocess.run(["git", "add", "history.txt"], check=True)

            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = commit_date
            env["GIT_COMMITTER_DATE"] = commit_date

            subprocess.run(["git", "commit", "-m", msg, "--quiet"], env=env, check=True)

    current_date += timedelta(days=1)