import os
import json

from github import Github
from dotenv import load_dotenv

load_dotenv()


def main():
    repo_name = "hyperledger/fabric"  # "corda/corda"
    g = Github(os.environ.get("GITHUB_ACCESS_TOKEN", None))
    repo = g.get_repo(repo_name)
    activities = repo.get_stats_commit_activity()

    output_list = []
    for each in activities:
        output_list.append({"total": each.total, "week": each.week.isoformat(), "repo": repo_name})

    with open(f"{repo_name.replace('/','_')}_stats_commit.json", "w") as f:
        json.dump(output_list, f)


if __name__ == "__main__":
    main()
