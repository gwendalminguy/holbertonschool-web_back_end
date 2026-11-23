-- Creates a stored procedure to compute an average score
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average FLOAT;

    -- Compute average score for user.
    SELECT AVG(score) INTO average
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update user row.
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END //

DELIMITER ;
