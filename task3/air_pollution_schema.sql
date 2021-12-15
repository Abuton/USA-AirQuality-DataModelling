CREATE TABLE IF NOT EXISTS `pollution-db2`.`AirQualityMeasures` (
  `id` INT NOT NULL,
  `DateRecorded` DATETIME NOT NULL,
  `SiteID` INT NOT NULL,
  `Location` VARCHAR(45) NOT NULL,
  `NO2` FLOAT NULL,
  `NOX` FLOAT NULL,
  `NO` FLOAT NULL,
  `PM10` FLOAT NULL,
  `PM2.5` FLOAT NULL,
  `NVPM10` FLOAT NULL,
  `NVPM2.5` FLOAT NULL,
  `VPM10` FLOAT NULL,
  `VPM2.5` FLOAT NULL,
  `CO` FLOAT NULL,
  `O3` FLOAT NULL,
  `Temperature` FLOAT NULL,
  `ReletiveHumidity` FLOAT NULL,
  `AirPressure` FLOAT NULL,
  `GeoPoint2d` VARCHAR(45) NULL,
  `CurrentStatus` VARCHAR(45) NULL,
  `InstrumentType` VARCHAR(45) NULL,
  `StartDateTime` DATETIME NULL,
  `EndDateTime` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;