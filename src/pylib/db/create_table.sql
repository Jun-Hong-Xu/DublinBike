-- SQL used to created required tables;

CREATE DATABASE `dbike`;

CREATE TABLE `station` (
  `sid` int(11) NOT NULL AUTO_INCREMENT COMMENT 'pk',
  `station_id` int(11) DEFAULT NULL ,
  `station_name` varchar(40) DEFAULT NULL,
  `station_address` varchar(50) DEFAULT NULL COMMENT 'address',
  `lat` float(10,6) DEFAULT NULL COMMENT 'latitude',
  `lng` float(10,6) DEFAULT NULL COMMENT 'longitude',
  `bike_stands` int(11) DEFAULT NULL COMMENT 'all stands',
  `ava_bikes` int(11) DEFAULT NULL COMMENT 'available bikes',
  `ava_stands` int(11) DEFAULT NULL COMMENT 'available stands',
  `status` ENUM('OPEN','CLOSED') DEFAULT 'OPEN',
  `update` timestamp DEFAULT NULL COMMENT 'data update time in API',
  /*`modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'last modify time',*/
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=6000000 DEFAULT CHARSET=utf8mb4;


CREATE TABLE `station_weather` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `station_id` int(11) DEFAULT NULL ,
  `lat` float(10,6) DEFAULT NULL,
  `lng` float(10,6) DEFAULT NULL,
  `weather_id` int(11) DEFAULT NULL COMMENT '3-digit id describe main weather',
  `temp` float(5,2) DEFAULT NULL COMMENT  'Celsius temperature',
  `feels_like` float(5,2) DEFAULT NULL COMMENT  'feels-like temperature in Celsius',
  `temp_min` float(5,2) DEFAULT NULL COMMENT  'Celsius temperature',
  `temp_max` float(5,2) DEFAULT NULL COMMENT  'Celsius temperature',
  `pressure` int(10) DEFAULT NULL COMMENT 'atm pressure,hPa',
  `humidity` int(10) DEFAULT NULL COMMENT 'humidity, %',
  `wind_speed` float(5,2) DEFAULT NULL COMMENT 'wind speed, m/s',
  `wind_deg` int(10) DEFAULT NULL COMMENT 'wind direction, degrees(meteorological)',
  `clouds` int(10) DEFAULT NULL COMMENT 'cloudiness, %',
  `rain_1h` float(5,2) DEFAULT NULL COMMENT 'rain volume for the last 1 hour, mm',
  `rain_3h` float(5,2) DEFAULT NULL COMMENT 'rain volume for the last 3 hour, mm',
  `snow_1h` float(5,2) DEFAULT NULL COMMENT 'snow volume for the last 1 hour, mm',
  `snow_3h` float(5,2) DEFAULT NULL COMMENT 'snow volume for the last 3 hour, mm',
  `update_time`timestamp DEFAULT NULL COMMENT 'data update time in API',
  `sid` int(10) DEAFAULT NULL COMMENT 'foreign key of table station, unique'
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;

