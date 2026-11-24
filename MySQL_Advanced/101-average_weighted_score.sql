-- Creates a stored procedure to compute all weighted average scores.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    -- Compute weighted average safely to update each user row.
    UPDATE users AS u
    JOIN (
        SELECT user_id, SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0) AS weighted_sum
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        GROUP BY user_id
    ) AS averages ON averages.user_id = u.id
    SET u.average_score = averages.weighted_sum;
END //

DELIMITER ;
