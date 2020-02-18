-- SQL used to created required tables;

CREATE DATABASE `dbike`;

CREATE TABLE `station` (
  `sid` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `stationid` int(11) DEFAULT NULL ,
  `lat` float(5,2) DEFAULT NULL COMMENT 'latitude',
  `lng` float(5,2) DEFAULT NULL COMMENT 'longitude',
  `stands` int(11) DEFAULT NULL COMMENT 'available stands',
  `bikes` int(11) DEFAULT NULL COMMENT 'available bikes',
  `status` ENUM('OPEN','CLOSED') DEFAULT 'OPEN',
  `update` timestamp DEFAULT NULL COMMENT 'data update time in API',
  `modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modify time',
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=6000000 DEFAULT CHARSET=utf8mb4;


CREATE TABLE `station_weather` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stationid` int(11) DEFAULT NULL ,
  `lat` int(11) DEFAULT NULL,
  `lng` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;

