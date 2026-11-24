-- Creates a stored procedure to compute a weighted average score.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE weighted_average FLOAT;

    -- Compute weighted average safely.
    SELECT SUM(c.score * p.weight) / NULLIF(SUM(p.weight), 0)
    INTO weighted_average
    FROM corrections AS c
    JOIN projects AS p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update user row.
    UPDATE users
    SET average_score = weighted_average
    WHERE users.id = user_id;
END //

DELIMITER ;
