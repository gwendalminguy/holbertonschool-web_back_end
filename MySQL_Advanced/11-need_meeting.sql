-- Creates a view of students whose score is less than 80 and have no recent meeting
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (
    last_meeting IS NULL
    OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
);
