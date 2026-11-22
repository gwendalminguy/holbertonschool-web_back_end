-- Creates the table users if not existing with columns id, email and name
CREATE TABLE IF NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(256),
	name VARCHAR(256)
);
