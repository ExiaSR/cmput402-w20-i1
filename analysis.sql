SELECT repo, AVG(Cast ((
    JulianDay(i.closed_at) - JulianDay(i.created_at)
) As Integer))
FROM issues as i
GROUP BY i.repo;

SELECT repo, AVG(total)
FROM (
    SELECT repo, SUM(total) as total, strftime("%m-%Y", week) as 'month-year'
    FROM commit_activity
    GROUP BY strftime("%m-%Y", week), repo
)
GROUP BY repo;
