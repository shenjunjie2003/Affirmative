12.25
    `Add: table client, profile_picture column in user`
    CREATE TABLE `client` (
        `user_id` int NOT NULL,
        `name` VARCHAR(256) NOT NULL,
        `pronoun` VARCHAR(256) NOT NULL,
        `city` VARCHAR(256) NOT NULL,
        `state` VARCHAR(256) NOT NULL,
        PRIMARY KEY (`user_id`)
    );

    ALTER TABLE `user` 
    ADD COLUMN `profile_picture` VARCHAR(512) NULL DEFAULT NULL;