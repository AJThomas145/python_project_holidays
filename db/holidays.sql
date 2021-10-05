DROP TABLE IF EXISTS attractions;
DROP TABLE IF EXISTS theme_parks;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    continent VARCHAR (255)
);

create table theme_parks (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN
);
CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    category VARCHAR (255),
    theme_park_id INT REFERENCES theme_parks(id) ON DELETE CASCADE
);

