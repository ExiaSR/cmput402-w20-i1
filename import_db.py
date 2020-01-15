import json

from peewee import *

sqlite_db = SqliteDatabase("cmput402_ass1.db", pragmas={"journal_mode": "wal"})


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = sqlite_db


class Issues(BaseModel):
    id = IntegerField(primary_key=True)
    repo = TextField()
    created_at = DateTimeField()
    closed_at = DateTimeField()

class CommitActivity(BaseModel):
    week = DateTimeField()
    total = IntegerField()
    repo = TextField()

    class Meta:
        table_name = 'commit_activity'

file_name = "corda_gh_issues.json" # "gh_issues.json"
def main():
    with open(file_name, "r") as f:
        issues_json = json.load(f)
        with sqlite_db.atomic():
            Issues.insert_many(issues_json).execute()

    with open("corda_corda_stats_commit.json", "r") as f:
        with sqlite_db.atomic():
            CommitActivity.insert_many(json.load(f)).execute()

    with open("hyperledger_fabric_stats_commit.json", "r") as f:
        with sqlite_db.atomic():
            CommitActivity.insert_many(json.load(f)).execute()


if __name__ == "__main__":
    main()
