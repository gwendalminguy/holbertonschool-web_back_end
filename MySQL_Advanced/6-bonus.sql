-- Creates a stored procedure to add a correction to a student
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
    DECLARE project_id INT DEFAULT NULL;

    -- Find existing project with its name.
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name
    LIMIT 1;

    -- Create it if it does not exist.
    IF project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (project_name);

        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert correction row.
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END //

DELIMITER ;
