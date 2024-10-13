CREATE DATABASE IF NOT EXISTS MBTAdb;

USE MBTAdb;

DROP TABLE IF EXISTS mbta_buses_new;

CREATE TABLE mbta_buses_new (
    record_num INT AUTO_INCREMENT PRIMARY KEY,
    bus_id VARCHAR(255) NOT NULL,
    latitude DECIMAL(11,8) NOT NULL,
    longitude DECIMAL(11,8) NOT NULL,
    route_num VARCHAR(10) NULL,
    bearing INT NULL,
    current_status VARCHAR(255) NULL,
    current_stop_sequence INT NULL,
    direction_id INT NULL,
    occupancy_status VARCHAR(255) NULL,
    updated_at DATETIME NULL,
    stop_id VARCHAR(50) NULL,
    trip_id VARCHAR(50) NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
