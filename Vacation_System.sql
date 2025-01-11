-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema vacation_system
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema vacation_system
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `vacation_system` DEFAULT CHARACTER SET utf8 ;
USE `vacation_system` ;

-- -----------------------------------------------------
-- Table `vacation_system`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vacation_system`.`roles` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(45) NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE INDEX `role_id_UNIQUE` (`role_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vacation_system`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vacation_system`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `firstname` VARCHAR(45) NULL,
  `lastname` VARCHAR(45) NULL,
  UNIQUE `email` VARCHAR(100) NULL,
  `password` VARCHAR(500) NULL,
  `date_of_birth` DATE NULL,
  `role` INT NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_id_UNIQUE` (`user_id` ASC) VISIBLE,
  INDEX `fk_users_roles_idx` (`role` ASC) VISIBLE,
  CONSTRAINT `fk_users_roles`
    FOREIGN KEY (`role`)
    REFERENCES `vacation_system`.`roles` (`role_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vacation_system`.`countries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vacation_system`.`countries` (
  `country_id` INT NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NULL,
  PRIMARY KEY (`country_id`),
  UNIQUE INDEX `country_id_UNIQUE` (`country_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vacation_system`.`vacations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vacation_system`.`vacations` (
  `vacation_id` INT NOT NULL AUTO_INCREMENT,
  `vacation_title` VARCHAR(45) NULL,
  `start_date` DATE NULL,
  `end_date` DATE NULL,
  `price` FLOAT NULL,
  `total_likes` INT NULL,
  `img_url` VARCHAR(250) NULL,
  `country` INT NOT NULL,
  PRIMARY KEY (`vacation_id`),
  UNIQUE INDEX `vacation_id_UNIQUE` (`vacation_id` ASC) VISIBLE,
  INDEX `fk_vacations_countries1_idx` (`country` ASC) VISIBLE,
  CONSTRAINT `fk_vacations_countries1`
    FOREIGN KEY (`country`)
    REFERENCES `vacation_system`.`countries` (`country_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `vacation_system`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vacation_system`.`likes` (
  `like_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `vacation_id` INT NOT NULL,
  PRIMARY KEY (`like_id`),
  UNIQUE INDEX `like_id_UNIQUE` (`like_id` ASC) VISIBLE,
  INDEX `fk_likes_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_likes_vacations1_idx` (`vacation_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vacation_system`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_vacations1`
    FOREIGN KEY (`vacation_id`)
    REFERENCES `vacation_system`.`vacations` (`vacation_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- Insert data into roles
-- -----------------------------------------------------
INSERT INTO `vacation_system`.`roles` (`role_name`) VALUES
('Admin'),
('User');

-- -----------------------------------------------------
-- Insert data into users
-- -----------------------------------------------------
INSERT INTO `vacation_system`.`users` (`firstname`, `lastname`, `email`, `password`, `date_of_birth`, `role`) VALUES
('Alice', 'Smith', 'alice.smith@example.com', 'password123', '1985-01-15', 1),
('Bob', 'Johnson', 'bob.johnson@example.com', 'password123', '1990-06-25', 1),
('Charlie', 'Brown', 'charlie.brown@example.com', 'password123', '1995-03-10', 2),
('Diana', 'White', 'diana.white@example.com', 'password123', '2000-12-05', 2);

-- -----------------------------------------------------
-- Insert data into countries
-- -----------------------------------------------------
INSERT INTO `vacation_system`.`countries` (`country_name`) VALUES
('United States'),
('Canada'),
('France'),
('Italy'),
('Germany'),
('Japan'),
('Australia'),
('Mexico'),
('Brazil'),
('South Africa');

-- -----------------------------------------------------
-- Insert data into vacations
-- -----------------------------------------------------
INSERT INTO `vacation_system`.`vacations` (`vacation_title`, `start_date`, `end_date`, `price`, `total_likes`, `img_url`, `country`) VALUES
('Beach Getaway', '2024-01-10', '2024-01-20', 1500.00, 0, 'https://example.com/beach.jpg', 1),
('Ski Adventure', '2024-02-15', '2024-02-25', 2000.00, 0, 'https://example.com/ski.jpg', 2),
('Paris Tour', '2024-03-01', '2024-03-10', 1800.00, 0, 'https://example.com/paris.jpg', 3),
('Rome Holiday', '2024-04-05', '2024-04-15', 1700.00, 0, 'https://example.com/rome.jpg', 4),
('Berlin Escape', '2024-05-10', '2024-05-20', 1600.00, 0, 'https://example.com/berlin.jpg', 5),
('Tokyo Experience', '2024-06-15', '2024-06-25', 2500.00, 0, 'https://example.com/tokyo.jpg', 6),
('Sydney Adventure', '2024-07-10', '2024-07-20', 2200.00, 0, 'https://example.com/sydney.jpg', 7),
('Mexico Fiesta', '2024-08-01', '2024-08-10', 1400.00, 0, 'https://example.com/mexico.jpg', 8),
('Brazil Carnival', '2024-09-05', '2024-09-15', 1300.00, 0, 'https://example.com/brazil.jpg', 9),
('Cape Town Safari', '2024-10-10', '2024-10-20', 1900.00, 0, 'https://example.com/capetown.jpg', 10),
('Mountain Retreat', '2024-11-01', '2024-11-10', 1200.00, 0, 'https://example.com/mountain.jpg', 1),
('Desert Oasis', '2024-12-05', '2024-12-15', 1100.00, 0, 'https://example.com/desert.jpg', 2);
