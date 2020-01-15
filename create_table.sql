DROP TABLE IF EXISTS issues;
DROP TABLE IF EXISTS commit_activity;

CREATE TABLE issues (
    id INTEGER PRIMARY KEY,
    repo TEXT,
    created_at REAL,
    closed_at REAL
);

CREATE TABLE commit_activity (
    week REAL,
    total INTEGER,
    repo TEXT
);
