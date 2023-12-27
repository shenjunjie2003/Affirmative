12.25
`Add: table client`
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

    Jenny:

    ALTER TABLE `care_navigator`
    ADD COLUMN `zip_code` VARCHAR(512) NULL DEFAULT NULL;
    
    ALTER TABLE `provider`
    ADD COLUMN `zip_code` VARCHAR(512) NULL DEFAULT NULL;

Jonny:
`Saved information`
    CREATE TABLE `saved_navigator` (
        `client_id` INT NOT NULL,
        `navigator_id` INT NOT NULL,
        PRIMARY KEY (`client_id`, `navigator_id`)
    );

    CREATE TABLE `saved_provider` (
        `client_id` INT NOT NULL,
        `provider_id` INT NOT NULL,
        PRIMARY KEY (`client_id`, `provider_id`)
    );

`Change to care navigator table`
    ALTER TABLE care_navigator ADD COLUMN self_description TEXT;
    ALTER TABLE care_navigator ADD COLUMN trans_caregiving_experience TEXT;
    ALTER TABLE care_navigator ADD COLUMN additional_experience TEXT;
    ALTER TABLE care_navigator ADD COLUMN state VARCHAR(256) NOT NULL;
    ALTER TABLE care_navigator ADD COLUMN city VARCHAR(256) NOT NULL;
    ALTER TABLE care_navigator DROP COLUMN location;
    ALTER TABLE care_navigator MODIFY insurance VARCHAR(256);
    ALTER TABLE care_navigator MODIFY zip_code VARCHAR(256);
    ALTER TABLE care_navigator MODIFY email VARCHAR(256);

`Jenny`
    ALTER TABLE `provider` 
    ADD COLUMN `finances` VARCHAR(512) NULL DEFAULT NULL;
    ALTER TABLE `provider` 
    ADD COLUMN `qualifications` VARCHAR(512) NULL DEFAULT NULL;
    ALTER TABLE provider
    ADD COLUMN profile_picture LONGBLOB;
