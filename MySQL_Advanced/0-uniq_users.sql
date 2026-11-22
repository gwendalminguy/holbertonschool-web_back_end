-- Creates the table users if not existing with columns id, email and name
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`email` VARCHAR(256) UNIQUE NOT NULL,
	`name` VARCHAR(256)
);
