-- Creates the table users if not existing with columns id, email, name and country
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	`id` INT AUTO_INCREMENT PRIMARY KEY,
	`email` VARCHAR(256) UNIQUE NOT NULL,
	`name` VARCHAR(256),
	`country` ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
