CREATE TABLE IF NOT EXISTS `guesses` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Time` varchar(45) NOT NULL,
  `Results` varchar(45) NOT NULL,
  `Lives_left` int NOT NULL,
  PRIMARY KEY (`ID`)
);