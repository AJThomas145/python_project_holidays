DROP TABLE IF EXISTS theme_parks;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS attractions;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    continent VARCHAR (255)
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    category VARCHAR (255)
);

create table theme_parks (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    country_id INT REFERENCES countries(id),
    attraction_id INT REFERENCES attractions(id),
    visited BOOLEAN
);