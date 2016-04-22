CREATE DATABASE capstone_sp;

CREATE TABLE events (
  id              SERIAL PRIMARY KEY,
  country         CHARACTER VARYING,
  subscriptionId  CHARACTER VARYING,
  source          CHARACTER VARYING,
  userId          BIGINT,
  eventType       INTEGER,
  nativeEventType CHARACTER VARYING,
  startTs         TIMESTAMP,
  endTs           TIMESTAMP,
  startCellId     CHARACTER VARYING,
  endCellId       CHARACTER VARYING,
  deviceType      CHARACTER VARYING,
  deviceId        CHARACTER VARYING,
  deviceTypeId    CHARACTER VARYING,
  countryCode     CHARACTER VARYING
);


COPY events (
  country,
  subscriptionId,
  source,
  userId,
  eventType,
  nativeEventType,
  startTs,
  endTs,
  startCellId,
  endCellId,
  deviceType,
  deviceId,
  deviceTypeId,
  countryCode
)
FROM '/Users/EH/columbia/projects/capstone_sp/data/events_sample_Columbia.csv'
WITH
DELIMITER '|' CSV
HEADER;

--### Cells ###--

CREATE TABLE cells (
  country         CHARACTER VARYING,
  cellID          CHARACTER VARYING,
  lac             INTEGER,
  universalCellid INTEGER,
  latitude        NUMERIC,
  longitude       NUMERIC,
  technology      CHARACTER VARYING,
  siteType        CHARACTER VARYING,
  sporadic        BOOLEAN,
  azimuth         CHARACTER VARYING,
  beamWidth       CHARACTER VARYING,
  frequency       INTEGER,
  antennaHeight   INTEGER,
  cellPower       INTEGER,
  cellRange       INTEGER,
  serviceTo       CHARACTER VARYING,
  "index"         INTEGER,
  id              SERIAL PRIMARY KEY
);

DROP TABLE cells;

COPY cells (
  country,
  cellID,
  lac,
  universalCellid,
  latitude,
  longitude,
  technology,
  siteType,
  sporadic,
  azimuth,
  beamWidth,
  frequency,
  antennaHeight,
  cellPower,
  cellRange,
  serviceTo,
  "index"
)
FROM '/Users/EH/columbia/projects/capstone_sp/data/cells_sample_Columbia.csv'
WITH
DELIMITER '|' CSV
HEADER;

-- Amenities
CREATE TABLE amenities(
  id SERIAL PRIMARY KEY,
  longitude NUMERIC,
  latitude NUMERIC,
  amenity CHARACTER VARYING
);

COPY amenities(
  longitude, latitude, amenity
) FROM '/Users/EH/columbia/projects/capstone_sp/data/amenities.csv'
WITH DELIMITER ',' CSV
HEADER ;
