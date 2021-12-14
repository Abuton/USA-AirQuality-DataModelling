-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pollution-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pollution-db` ;
USE `pollution-db` ;

-- -----------------------------------------------------
-- Table `pollution-db`.`stations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`stations` (
  `SiteID` INT NOT NULL,
  `Location` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `SiteID_UNIQUE` (`SiteID` ASC) VISIBLE,
  UNIQUE INDEX `Location_UNIQUE` (`Location` ASC) VISIBLE,
  PRIMARY KEY (`SiteID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `pollution-db`.`WeatherCondition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`WeatherCondition` (
  `id` INT NOT NULL,
  `SiteID` INT NOT NULL,
  `Temperature` FLOAT NULL,
  `ReletiveHumidity` FLOAT NULL,
  `AirPressure` FLOAT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_WeatherCondition_1_idx` (`SiteID` ASC) VISIBLE,
  CONSTRAINT `fk_WeatherCondition_1`
    FOREIGN KEY (`SiteID`)
    REFERENCES `pollution-db`.`stations` (`SiteID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
COMMENT = '\n\nStore Weather Condition';


-- -----------------------------------------------------
-- Table `pollution-db`.`InstrumentCondition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`InstrumentCondition` (
  `id` INT NOT NULL,
  `SiteID` INT NOT NULL,
  `CurrentStatus` VARCHAR(45) NULL,
  `InstrumentType` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_InstrumentCondition_1_idx` (`SiteID` ASC) VISIBLE,
  CONSTRAINT `fk_InstrumentCondition_1`
    FOREIGN KEY (`SiteID`)
    REFERENCES `pollution-db`.`stations` (`SiteID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`AirQualityMeasures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`AirQualityMeasures` (
  `id` INT NOT NULL,
  `SiteID` INT NOT NULL,
  `NO2` FLOAT NULL,
  `NOX` FLOAT NULL,
  `NO` FLOAT NULL,
  `PM10` FLOAT NULL,
  `PM2.5` FLOAT NULL,
  `NVPM` FLOAT NULL,
  `NVPM2.5` FLOAT NULL,
  `VPM10` FLOAT NULL,
  `VPM2.5` FLOAT NULL,
  `CO` FLOAT NULL,
  `O3` FLOAT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_AirQualityMeasures_1_idx` (`SiteID` ASC) VISIBLE,
  CONSTRAINT `fk_AirQualityMeasures_1`
    FOREIGN KEY (`SiteID`)
    REFERENCES `pollution-db`.`stations` (`SiteID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pollution-db`.`DateInformation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pollution-db`.`DateInformation` (
  `DateRecorded` DATETIME NOT NULL,
  `SiteID` INT NULL,
  `StartDateTime` DATETIME NULL,
  `EndDateTime` DATETIME NULL,
  PRIMARY KEY (`DateRecorded`),
  INDEX `fk_DateInformation_1_idx` (`SiteID` ASC) VISIBLE,
  CONSTRAINT `fk_DateInformation_1`
    FOREIGN KEY (`SiteID`)
    REFERENCES `pollution-db`.`stations` (`SiteID`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
