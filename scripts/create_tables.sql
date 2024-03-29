CREATE DATABASE IF NOT EXISTS MALNotifier;

USE MALNotifier;

CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL, 
    `facebook` INT,
    `mal` VARCHAR(255) NOT NULL,
    `ova` BOOLEAN NOT NULL DEFAULT FALSE,
    `unaired` BOOLEAN NOT NULL DEFAULT TRUE,
    `minRating` INT NOT NULL DEFAULT 0,
    UNIQUE (`mal`),
    UNIQUE (`facebook`),
    UNIQUE (`email`),
    PRIMARY KEY(`id`)
); 

CREATE TABLE IF NOT EXISTS `shows` (
    `showId` INT NOT NULL,
    `sequel` INT,
    `xml` MEDIUMTEXT,
    `lastXmlUpdate` INT,
    PRIMARY KEY(`showId`)
);

CREATE TABLE IF NOT EXISTS `titles` (
    `titleId` INT NOT NULL AUTO_INCREMENT,
    `showId` INT NOT NULL,
    `title` VARCHAR(2000),
    PRIMARY KEY(`titleId`),
    FOREIGN KEY (`showId`) REFERENCES `shows` (`showId`) ON DELETE CASCADE ON UPDATE CASCADE
);
