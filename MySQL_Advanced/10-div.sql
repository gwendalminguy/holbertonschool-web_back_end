-- Creates a function that safely divides a number by another
DELIMITER //

CREATE FUNCTION SafeDiv (
    num1 INT,
    num2 INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;

    IF num2 = 0 THEN
        SET result = 0;
    ELSE
        SET result = num1 / num2;
    END IF;

    RETURN result;
END //

DELIMITER ;
