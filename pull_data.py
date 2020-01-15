import os
import json
import time
from datetime import datetime
from github import Github
from dotenv import load_dotenv

load_dotenv()

def main():
    g = Github(os.environ.get('GITHUB_ACCESS_TOKEN', None))

    repo_name = "corda/corda" # "hyperledger/fabric"
    repo = g.get_repo("corda/corda")
    issues_list = []
    for issue in repo.get_issues(state="all", since=datetime.strptime("2019-01-15T00:00:00Z", "%Y-%m-%dT%H:%M:%S%z")):
        if issue.closed_at:
            issues_list.append(
                {"id": issue.id, "created_at": issue.created_at.isoformat(), "closed_at": issue.closed_at.isoformat(), "repo": repo_name}
            )

    for pulls in repo.get_pulls(state="all"):
        if pulls.closed_at:
            issues_list.append(
                {"id": pulls.id, "created_at": pulls.created_at.isoformat(), "closed_at": pulls.closed_at.isoformat(), "repo": repo_name}
            )

    with open("corda_gh_issues.json", "w") as f:
        json.dump(issues_list, f)


if __name__ == "__main__":
    main()
