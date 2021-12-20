CREATE TABLE `User` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_name` VARCHAR(100) NOT NULL,
	`user_id` VARCHAR(100) NOT NULL UNIQUE,
	`coin` INT NOT NULL DEFAULT 100,
	`role` VARCHAR(200),
    PRIMARY KEY (`id`)
);

CREATE TABLE `Proposal` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `time` DATETIME,
    `user_name` VARCHAR(100) NOT NULL,
    `user_id` VARCHAR(100) NOT NULL,
    `event` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id`)
)
